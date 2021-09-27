
from ansible.module_utils.basic import AnsibleModule

import traceback
import re




def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=dict(
            regex=dict(required=True),
            lines=dict(required=True),
        )
    )
    regex = module.params['regex']
    value = module.params['lines']
    #regex = r"^\s(.*)"
    regex=r"%s" % regex



    response = dict(
        changed=False,
        result=[]
    )
    result=[]
    try:
        matches = re.finditer(regex, value, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            result.append(match.group().strip())


    except Exception as e:
        module.fail_json(msg="Error while searching:\n{}".format(traceback.format_exc()))
        return
    response["result"] = result
    response["changed"] = True
    module.exit_json(**response)

if __name__ == "__main__":
    main()

