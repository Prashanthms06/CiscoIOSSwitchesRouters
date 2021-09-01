from ansible.module_utils.common.collections import ImmutableDict
from jinja2 import Environment, FileSystemLoader

from callback_plugins.logger import Logger
from callback_plugins.rest_operations import Request, PUT_OPERATION, HttpRequest
import os

SERVICE_NOW_PROPERTY="servicenow"
SERVICE_NOW_TICKET_UPDATE_URI='sn_ticket_update_uri'
SERVICE_NOW_REQUEST_SYSID='request_sysid'
SERVICE_NOW_TABLE_UPDATE_URI='sn_table_update_uri'
SERVICE_NOW_REQUEST_STATUS = ImmutableDict(CloseIncomplete=4, CloseComplete=3)
SERVICE_NOW_AUTH='sn_auth'

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class ServiceNow:
    '''
    Class responsible for calling the ServiceNow apis
    '''
    def __init__(self,variable_manager):
        self.vm = variable_manager

    def _all_parameters_present(self,result):
        '''
        Method to check if all the necessary service request parameters are present or not.
        :return: boolean
        '''
        #import pdb
        #pdb.set_trace()
        all_parameters_present=True
        #Check if the service now update request uri is present or not
        if not SERVICE_NOW_TICKET_UPDATE_URI in self.vm.get_vars()['hostvars'][result._host.name] :
            Logger.log("Property {0} is not defined. Hence ServiceNow will not be updated.".format(SERVICE_NOW_TICKET_UPDATE_URI))
            all_parameters_present=False

        if not SERVICE_NOW_PROPERTY in self.vm.get_vars()['hostvars'][result._host.name]:
            Logger.log(
                "Property {0}  is not defined. Hence ServiceNow will not be updated.".format(SERVICE_NOW_PROPERTY))
            all_parameters_present = False

        # Check if the service now request's sysid is present or not. This is an important parameters
        if not SERVICE_NOW_REQUEST_SYSID in self.vm.get_vars()['hostvars'][result._host.name][SERVICE_NOW_PROPERTY]:
            Logger.log("Property {0}  is not defined. Hence ServiceNow will not be updated.".format(SERVICE_NOW_REQUEST_SYSID))
            all_parameters_present=False

        if not SERVICE_NOW_AUTH in self.vm.get_vars()['hostvars'][result._host.name]:
            Logger.log(
                "Property {0}  is not defined. Hence ServiceNow will not be updated.".format(SERVICE_NOW_AUTH))
            all_parameters_present = False

        #Check if username and password fields are present
        if not 'username' in self.vm.get_vars()['hostvars'][result._host.name][SERVICE_NOW_AUTH]:
            Logger.log(
                "Property {0}  is not defined for authentication. Hence ServiceNow will not be updated.".format('username'))
            all_parameters_present = False

        if not 'password' in self.vm.get_vars()['hostvars'][result._host.name][SERVICE_NOW_AUTH]:
            Logger.log(
                "Property {0}  is not defined for authentication. Hence ServiceNow will not be updated.".format('password'))
            all_parameters_present = False

        #username and passwords must not be empty
        username = self.vm.get_vars()['hostvars'][result._host.name][SERVICE_NOW_AUTH]['username']
        password = self.vm.get_vars()['hostvars'][result._host.name][SERVICE_NOW_AUTH]['password']
        if username.strip()=="":
            Logger.log(
                "Property {0}  is  empty for authentication. Hence ServiceNow will not be updated.".format(
                    'username'))
            all_parameters_present = False

        if password.strip()=="":
            Logger.log(
                "Property {0}  is  empty for authentication. Hence ServiceNow will not be updated.".format(
                    'password'))
            all_parameters_present = False

        return all_parameters_present

    def update_request_as_fail(self,result):
        '''
        This method will update the ServiceNow with status incomplete
        :return:
        '''
        if not self._all_parameters_present(result):
            return

        failed_msg = result._result['msg']
        sn_ticket_update_uri = self.vm.get_vars()['hostvars'][result._host.name][SERVICE_NOW_TICKET_UPDATE_URI]
        Logger.log("Received servicenow request uri as: {0}".format(sn_ticket_update_uri))
        # check if there is sysid is provided as part of the request
        sn_request_sysid = self.vm.get_vars()['hostvars'][result._host.name][SERVICE_NOW_PROPERTY][
            SERVICE_NOW_REQUEST_SYSID]
        Logger.log("Received servicenow request sysid as: {0}".format(sn_request_sysid))
        Logger.log("Closing the service now request with sysid:{0} with status {1}".format(sn_ticket_update_uri, str(
            SERVICE_NOW_REQUEST_STATUS['CloseIncomplete'])))
        # let's call the api
        url = sn_ticket_update_uri + sn_request_sysid
        Logger.log("Servicenow request final update url is {0}".format(url))
        j2_env = Environment(loader=FileSystemLoader(CURRENT_DIRECTORY), trim_blocks=True)
        service_now_data = j2_env.get_template('service_now_request.j2').render(
            state=SERVICE_NOW_REQUEST_STATUS['CloseIncomplete'],
            message=failed_msg
        )
        Logger.log("Put operation data for url {0} is {1}".format(url, service_now_data))

        username = self.vm.get_vars()['hostvars'][result._host.name][SERVICE_NOW_AUTH]['username']
        password = self.vm.get_vars()['hostvars'][result._host.name][SERVICE_NOW_AUTH]['password']

        request_object = Request(PUT_OPERATION). \
            set_url(url). \
            set_data(service_now_data). \
            set_basic_auth(username, password)
        response = HttpRequest().perform_operation(request_object)

        Logger.log("Status code for put operation of url {0} with data {1} is {2}".format(url,
                                                                                          service_now_data,
                                                                                          response.get_response().status_code))