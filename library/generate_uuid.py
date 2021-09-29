import uuid

from ansible.module_utils.basic import AnsibleModule

import traceback
import re

def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=dict(
        )
    )

    response = dict(
        changed=False,
        uuid=""
    )

    response["uuid"] = str(uuid.uuid4())
    response["changed"] = True
    module.exit_json(**response)

if __name__ == "__main__":
    main()

