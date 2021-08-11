[Main Menu](../README.md)
# VLAN Configuration 


| Parameters | Mandatory/Optional |Remarks |
| ------ | ---------- |----------|
| config_type | Mandatory | Type of the configuration.For this use case, value of this parameter would be vlan_configuration |
| operation_type |Mandatory | Type of the operation. Vlan  configuration currently supports only create operation |
| config | Mandatory| Configuration to be used.|

## Without SVI (Switched Virtual Interface)
Use the following sample ansible command to create a vlan without assigning svi
```shell
ansible-playbook cisco_ios.yml -i inventory -e \
'{
"config_type":"vlan_configuration",
"operation_type":"create",
"config":
         [
            {"name":"Vlan_30","vlan_id":50}
         ]
 }'
```

## With SVI (Switched Virtual Interface)
Use the following sample ansible command to create vlan by assigning an ip address and ip mask

```shell
ansible-playbook  cisco_ios.yml -i inventory -e '{
"config_type":"vlan_configuration",
"operation_type":"create",
"config":[
            {"name":"Vlan_50","vlan_id":50,"ipv4addr":"10.2.0.1","ip_mask":"255.255.255.0"}
         ]
}'

```

