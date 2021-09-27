[Main Menu](../README.md)
# Layer3 Configuration


| Parameters | Mandatory/Optional |Remarks |
| ------ | ---------- |----------|
| config_type | Mandatory | Type of the configuration.For this use case, value of this parameter would be vlan_configuration |
| operation |Mandatory | Type of the operation. Vlan  configuration currently supports only create operation |
| config | Mandatory| Configuration to be used.|
| description | Optional | Add Description into the Interface| 

## 
Use the following sample ansible command to add layer3 config into physical interface
```shell
ansible-playbook cisco_ios.yml -i inventory -e '{
"config_type":"L3_configuration",
"operation":"create",
"config":[
            {
                "name":"GigabitEthernet1/0/18",
                "ipv4addr":"10.6.0.1",
                "ip_mask":"255.255.255.0",
                "ipv6addr":"2001:df3:bf80:4285:10:152:120:222/64",
                "description": "Creating via ansible"
                }
         ]
}'
```

