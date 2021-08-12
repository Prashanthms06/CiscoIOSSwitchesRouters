import ipaddress
from ansible.module_utils.basic import AnsibleModule
import traceback


def main():
    module = AnsibleModule(
        supports_check_mode=True,
         argument_spec=dict(
            vlan_range=dict(required=True)
        )
    )
    vlan_range = module.params['vlan_range']


    response = dict(
        changed=False,
    )
    splits = vlan_range.split("-")
    for vlan in splits:
        try:
            #converting to integer should be sufficient
            int(vlan)
        except:
            module.fail_json(msg="Vlan {} is not integer:\n{}".format(vlan, traceback.format_exc()))
            return

    response["changed"] = True
    module.exit_json(**response)

if __name__ == "__main__":
    main()

