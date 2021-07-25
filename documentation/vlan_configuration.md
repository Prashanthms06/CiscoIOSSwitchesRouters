[Main Menu](../README.md)
# VLAN Configuration 
## Without SVI (Switched Virtual Interface)

```shell
ansible-playbook cisco_ios.yml -i inventory -e '{"config_type":"vlan_configuration","operation_type":"create","config":[{"name":"Vlan_30","vlan_id":50}]}'
```

## With SVI (Switched Virtual Interface)
```shell
ansible-playbook cisco_ios.yml -i inventory -e '{"config_type":"vlan_configuration","operation_type":"create","config":[{"name":"Vlan_30","vlan_id":50}]}'

```

