
import requests


from requests.auth import HTTPBasicAuth

from callback_plugins.logger import Logger

PUT_OPERATION="put"
POST_OPERATION="post"
GET_OPERATION="get"
DELETE_OPERATION="delete"

class Request:
    def __init__(self, request_type):
        self.headers = None
        self.request_type = request_type
        self.error=None

    def set_url(self, url):
        self.url = url
        return self

    def set_data(self,data):
        self.data=data
        return self

    def get_request_type(self):
        return self.request_type

    def get_url(self):
            return self.url

    def get_headers(self):
        return self.headers

    def add_header(self, key, value):
        self.headers[key] =value

    def get_data(self):
        return self.data

    def set_basic_auth(self,username, password):
        self.auth = HTTPBasicAuth(username, password)
        return self

    def get_auth(self):
        return self.auth


class Response:
    """
    This class is responsible for holding the actual response returned while calling external url/uri.
    Also consumers of this class can set the error codes etc so that the callee knows if there was any error occurred
    while performing the operation.
    """
    def __init__(self):
        #set this variable to true, to indicate if there are any errors while performing the operation.
        self.is_error = False

    def set_response(self, http_response):
        """
        Set the requests.Response object
        :param http_response:
        """
        self.http_response = http_response

    def set_error(self, err):
        """
        Use this method to set the error. Calling this method will set the variable isError = True and this
        means that there has been error while performing the operation.
        """
        self.is_error = True
        self.error = err

    def has_error(self):
        """
        Returns whether error has occured or not
        :return: True or False
        """
        return self.is_error


    def get_response(self):
        """
        Returns the response object from the python's request module
        :return: requests.Response object
        """
        return self.http_response


    def get_error_response(self):
        """
        Returns the error object
        :return:
        """
        return self.error

class HttpRequest:
    """
    This class is responsible for making REST calls to the external URL/ URI using python's request module.
    User of this class must pass rest.Request.Request object to the  performOP method. Based on the type of the
    request set (put,post,get) corresponding method's will be called.
    Currently this class supports only put, post and get operations.
    """

    # Method to perform the acutal operation
    def perform_operation(self, request):
        """
        This method should be called for performing Http operations like GET,PUT or POST.  All the necessary things like
        headers, url etc should be set in the rest.Request.Request object which is passed as argument to this method.
        :param request: rest.Request.Request
        :return:
        """
        Logger.log("Performing operation of type {0}  with url {1}".format(request.get_request_type(),request.get_url()))


        request_type = request.get_request_type()
        if request_type == PUT_OPERATION:
            return self.__perform_put(request)
        elif request_type == POST_OPERATION:
            return self.__perform_post(request)
        elif request_type == GET_OPERATION:
            return self.__perform_get(request)
        else:
            raise Exception("Unknown request type {}".format(request_type))

    def __perform_put(self, request):
        """
        Method to call put operation on an external url/uri
        :param request: rest.Request.Request
        :return: rest.Request.Response
        """
        # create the response to be returned
        resp = Response()
        Logger.log(
            "Performing put operation  with url {0} with data {1}".format(request.get_url(),request.get_data()))
        try:
            #for supresssing the warning
            requests.packages.urllib3.disable_warnings()
            response = requests.put(request.get_url(), data=request.get_data(),
                                    headers=request.get_headers(), verify=False,auth=request.get_auth())
            Logger.log("Status code of put operation {0} is {1}".format(request.get_url(), response.status_code))
            #set the actual response
            resp.set_response(response)
        except requests.exceptions.HTTPError as errh:
            Logger.log(
                "Exception {0} while putting the data {1}. Not processing further".format(errh, request.get_data()))
            #set the error response and indicate that error has occured
            resp.set_error(errh)

        except requests.exceptions.ConnectionError as errc:
            Logger.log(
                "Exception {0} while putting the data {1}. Not processing further".format(errc, request.get_data()))
            # set the error response and indicate that error has occured
            resp.set_error(errc)
        except requests.exceptions.Timeout as errt:
            Logger.log(
                "Exception {0} while putting the data {1}. Not processing further".format(errt, request.get_data()))
            # set the error response and indicate that error has occured
            resp.set_error(errt)
        # Catch all the exception which are uncaught
        except requests.exceptions.RequestException as err:
            Logger.log("Exception {0} while putting the data {1}. Not processing further".format(err.response,
                                                                                                 request.get_data()))
            # set the error response and indicate that error has occured
            resp.set_error(err)

        return resp

    def __perform_post(self, request):
        # create the response to be returned
        resp = Response()
        Logger.log("Performing post operation with url {0} with data {1}".format(request.get_url(), request.get_data()))
        try:
            requests.packages.urllib3.disable_warnings()
            response = requests.post(request.get_url(), data=request.get_data(),
                                     headers=request.get_headers(), verify=False,auth=request.get_auth())
            Logger.log("Status code of post operation {0} is {1}".format(request.get_url(), response.status_code))
            resp.set_response(response)
        except requests.exceptions.HTTPError as errh:
            Logger.log(
                "Exception {0} while posting ".format(errh))
            #set the error response and indicate that error has occured
            resp.set_error(errh)

        except requests.exceptions.ConnectionError as errc:
            Logger.log(
                "Exception {0} while posting ".format(errc))
            # set the error response and indicate that error has occured
            resp.set_error(errc)
        except requests.exceptions.Timeout as errt:
            Logger.log(
                "Exception {0} while posting ".format(errt))
            # set the error response and indicate that error has occured
            resp.set_error(errt)
        # Catch all the exception which are uncaught
        except requests.exceptions.RequestException as err:
            Logger.log("Exception {0} while putting the data {1}. Not processing further".format(err.response,
                                                                                                 request.get_data()))
            # set the error response and indicate that error has occured
            resp.set_error(err)

        return resp


    def __perform_get(self, request):
        # create the response to be returned
        resp = Response()
        Logger.log("Performing get operation with url {0} ".format(request.get_url()))
        try:
            requests.packages.urllib3.disable_warnings()
            response = requests.get(request.get_url(), headers=request.get_headers(), verify=False,auth=request.get_auth())
            Logger.log("Status code of get operation {0} is {1}".format(request.get_url(), response.status_code))
            resp.set_response(response)
        except requests.exceptions.HTTPError as errh:
            Logger.log(
                "Exception {0} while performing GET operation".format(errh))
            # set the error response and indicate that error has occured
            resp.set_error(errh)

        except requests.exceptions.ConnectionError as errc:
            Logger.log(
                "Exception {0} while performing GET operation".format(errc))
            # set the error response and indicate that error has occured
            resp.set_error(errc)
        except requests.exceptions.Timeout as errt:
            Logger.log(
                "Exception {0} while performing GET operation".format(errt))
            # set the error response and indicate that error has occured
            resp.set_error(errt)
        # Catch all the exception which are uncaught
        except requests.exceptions.RequestException as err:
            Logger.log(
                "Exception {0} while performing GET operation".format(err))
            # set the error response and indicate that error has occured
            resp.set_error(err)

        return resp