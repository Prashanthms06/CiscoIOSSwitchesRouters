import re
class FilterModule(object):
    def extract_entity(self,lines, regex):
        regex = r"%s" % regex
        result = []
        matches = re.finditer(regex, lines, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            result.append(match.group().strip())
        return result

    def filters(self):
        return {
            'extract_entity': self.extract_entity,
        }