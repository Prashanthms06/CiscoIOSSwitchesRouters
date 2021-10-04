#This filter plugin will be used to send the HTML code for right and wrong based on the presence and absence of
#key words. This funtion will be used in in reporting. As of 4th Oct 2021, this function is used for generating
#summary of hosts while doing upgradation

import json

from jsonpath_rw import jsonpath
from jsonpath_rw_ext import parse

# for calling extended methods
import jsonpath_rw_ext as jp

HTML5_RIGHT_SYMBOL='&#9989;'
HTML5_CROSS_SYMBOL='&#10060;'

class FilterModule(object):
    def fetch_symbol(self,host,hostvars,field_name):
        # if the field name is present and the failed is not false
        if  field_name in  hostvars[host] and not hostvars[host][field_name]['failed']:
            return HTML5_RIGHT_SYMBOL
        else:
            return HTML5_CROSS_SYMBOL

    def fetch_value(self,json_data,json_path):
        return jp.match1(json_path,json_data)

    def interface_status(self,value):
        if value=="connected":
            return HTML5_RIGHT_SYMBOL
        else:
            return HTML5_CROSS_SYMBOL

    def filters(self):
        return {
            'fetch_symbol': self.fetch_symbol,
            'fetch_value': self.fetch_value,
            'interface_status': self.interface_status
        }