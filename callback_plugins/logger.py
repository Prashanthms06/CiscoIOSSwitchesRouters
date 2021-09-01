import time

from ansible.module_utils._text import to_bytes
TIME_FORMAT = "%b %d %Y %H:%M:%S"
MSG_FORMAT = "%(now)s  - %(data)s\n\n"
LOG_FILE_NAME="/tmp/callback.log"
class Logger:
    '''
    Helper method to log the message
    '''
    @staticmethod
    def log(message):
        '''
        Helper method to log the message to a file
        :param msg:
        :return:
        '''
        now = time.strftime(TIME_FORMAT, time.localtime())
        msg = to_bytes(MSG_FORMAT % dict(now=now, data=message))
        with open(LOG_FILE_NAME, "ab") as fd:
            fd.write(msg)