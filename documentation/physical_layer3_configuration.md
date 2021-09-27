[Main Menu](../README.md)
# Physical Layer3 Configuration


| Parameters | Mandatory/Optional |Remarks |
| ------ | ---------- |----------|
| config_type | Mandatory | Type of the configuration.For this use case, value of this parameter would be physical_layer |
| operation |Mandatory | Type of the operation. Currently only create operation is supported |
| config | Mandatory| Configuration to be used.|
| description | Optional | Add Description into the layer 3| 

## 
Use the following sample ansible command to add layer3 config into physical interface
```shell
ansible-playbook cisco_ios.yml -i inventory -e '{
"config_type":"PHYSICAL_LAYER3",
"operation":"create",
"config":[
            {
                "name":"GigabitEthernet1/0/18",
                "ipv4addr":"10.6.0.1",
                "ip_mask":"255.255.255.0",
                "description": "Creating via ansible"
                }
         ]
}'
```

