import re
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

        regex = r"%s" % regex
        result = []
        matches = re.finditer(regex, lines, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            result.append(match.group().strip())
        return result

    def filters(self):
        return {
            'compare_dict': self.compare_dict,
        }

    def _compare_l3(self):
        result={}
        return result

    de

