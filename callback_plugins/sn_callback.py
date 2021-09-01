
from ansible.plugins.callback import CallbackBase

__metaclass__ = type

from callback_plugins.rest_operations import Request, PUT_OPERATION, HttpRequest
from callback_plugins.servicenow import ServiceNow

DOCUMENTATION = '''
    name: ServiceNow
    short_description: Updating service now
    description:
        - This custom callback for PSA will update the service now tickets
'''
#get result output


class CallbackModule(CallbackBase):
    '''
        This callback plugin will perform the following operations:
        1. In case of failure of any tasks, it will update the ServiceNow with incomplete status
            Remarks: ServiceNow will send the sysid, using which the request status needs to be updated.

        2. In case of playbook success, it will update the ServiceNow with complete status
            2.1 In case of create operation, we will use ServiceNow table API to create a row
            2.2 In case of update operation, we will use ServiceNow table API to updata a row.
            2.3 In case of delete operation, we will use ServiceNow table API to delete a row.

            Remarks: In both update and delete operation sysid will be sent from ServiceNow. This sysId
            has to be used for doing update and delete operations.

        3. Once the playbook ends, we will send successfull or failure emails to the respective parties.
        '''

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'ServiceNowPlugin'
    # We need to enable this plugin to use it.
    CALLBACK_NEEDS_ENABLED = True

    def set_options(self, task_keys=None, var_options=None, direct=None):
        ''' override to set self.tree '''
        super(CallbackModule, self).set_options(task_keys=task_keys, var_options=var_options, direct=direct)

    def __init__(self, *args, **kwargs):
        super(CallbackModule, self).__init__(*args, **kwargs)

    def v2_playbook_on_play_start(self, play):
        #save the variable manager to get the variables
        self.vm = play.get_variable_manager()
        self.sn = ServiceNow(self.vm)

    def v2_runner_on_failed(self, result, *args, **kwargs):
        '''
        This method will be called when there is any failure while running the playbook.
        If there is any failure while running a playbook, ServiceNow will be updated with the Incomplete status
        :param result:
        :param args:
        :param kwargs:
        :return:
        '''
        #result._host.name will be localhost in case of infobloxl, aci, algosec
        self.sn.update_request_as_fail(result)



