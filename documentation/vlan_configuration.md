[Main Menu](../README.md)
# VLAN Configuration 


| Parameters | Mandatory/Optional |Remarks |
| ------ | ---------- |----------|
| config_type | Mandatory | Type of the configuration.For this use case, value of this parameter would be vlan_configuration |
| operation |Mandatory | Type of the operation. Vlan  configuration currently supports only create operation |
| config | Mandatory| Configuration to be used.|

## Without SVI (Switched Virtual Interface)
Use the following sample ansible command to create a vlan without assigning svi
```shell
ansible-playbook cisco_ios.yml -i inventory -e \
'{
"config_type":"vlan_configuration",
"operation":"create",
"config":
         [
            {"name":"Vlan_30","vlan_id":50}
         ]
 }'
```

## With SVI (Switched Virtual Interface)
Use the following sample ansible command to create vlan by assigning an ip4 address and ip mask

```shell
ansible-playbook  cisco_ios.yml -i inventory -e '{
"config_type":"vlan_configuration",
"operation":"create",
"config":[
            {"name":"Vlan_50","vlan_id":50,"ipv4addr":"10.2.0.1","ip_mask":"255.255.255.0"}
         ]
}'

Use the following sample ansible command to create vlan by assigning an ipv6 and ipv4
```shell

ansible-playbook  cisco_ios.yml -i inventory -e '{
"config_type":"vlan_configuration",
"operation":"create",
"config":[
            {
                "name":"Vlan_99",
                "vlan_id":99,
                "ipv4addr":"10.6.0.1",
                "ip_mask":"255.255.255.0",
                "ipv6addr":"2001:df3:bf80:4285:10:152:120:222/64",
                "description": "Creating via ansible"
                }
         ]
}'
```

Once the playbook runs successfully, you can login to the device and run the following command to verify
```shell

show run interface vlan <vlan_id>
```
![img.png](img.png)


for deleting vlan
```shell
> configure terminal
> no vlan <vlan_id> 
```
