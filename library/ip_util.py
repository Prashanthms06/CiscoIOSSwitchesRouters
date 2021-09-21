import ipaddress
from ansible.module_utils.basic import AnsibleModule
from ipaddress import  IPv6Interface,IPv4Interface
import traceback


def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=dict(
            ip_address=dict(required=True),
            type=dict(required=True),
        )
    )
    ip_val = module.params['ip_address']
    ip_type = module.params['type'].lower()

    module.log("Validating the ip address {0} of type {1}".format(ip_val,ip_type))

    response = dict(
        changed=False,
        network='',
        hostmask='',
        netmask=''
    )
    try:
        if ip_type == 'ipv4':
            interface = IPv4Interface(unicode(ip_val))
        elif ip_type == 'ipv6':
            #interface = ipaddress.ip_address(ip_val)
            interface = IPv6Interface(ip_val)
        else:
            module.fail_json(msg="Invalid ip type {} provide. Supported values are ipv4 and ipv6 only:\n{}".format(ip_type,traceback.format_exc()))
            return

    except Exception as e:
        module.fail_json(msg="Error converting the ip address:\n{}".format(traceback.format_exc()))
        return
    response["network"] = str(interface.network)
    response["hostmask"] = str(interface.hostmask)
    response["netmask"] = str(interface.netmask)
    response["changed"] = True
    module.exit_json(**response)

if __name__ == "__main__":
    main()

