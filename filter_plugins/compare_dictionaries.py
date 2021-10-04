import re
import sys

from ansible.errors import AnsibleError
try:
    import deepdiff
    HAS_DIFF = True
except ImportError:
    HAS_DIFF = False

try:
    import json
    HAS_JSON = True
except ImportError:
    HAS_JSON = False


class FilterModule(object):
    def compare_dict(self,expected, actual,type):
        if not HAS_DIFF:
            raise AnsibleError('compare_dict filter requires deepdiff library to be installed')

        if not HAS_JSON:
            raise AnsibleError('compare_dict filter requires JSON library to be installed')
        if not type=='running_config':
            return deepdiff.DeepDiff(expected, actual)
        else:
            return self._compare_run_cfg(expected,actual)

    def filters(self):
        return {
            'compare_dict': self.compare_dict,
        }
    def _compare_run_cfg(self,expected,actual):
        '''
        Taking the difference of running config
        :param expected:
        :param actual:
        :return:
        '''
        splitA = set(expected.split("\n"))
        splitB = set(actual.split("\n"))
        diff = splitB.difference(splitA)
        self.display(diff)
        return diff

    def display(self,msg):
        sys.stdout.write(msg)
        sys.stdout.flush()



