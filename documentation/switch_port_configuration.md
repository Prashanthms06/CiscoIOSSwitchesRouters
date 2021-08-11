[Main Menu](../README.md)
# Switch port configuration 

| Parameters | Mandatory/Optional |Remarks |
| ------ | ---------- |----------|
| config_type | Mandatory | Type of the configuration.For this use case, value of this parameter would be switch_port_configuration |
| operation_type |Mandatory | Type of the operation. Switch port configuration currently supports only create operation |
| config | Mandatory| Configuration to be used.|

Command to assign a port to a vlan in an access mode

```shell
ansible-playbook cisco_ios.yml -i inventory -e \
'{
"config_type":"switch_port_configuration",
"operation_type":"create",
"config":[
          {"name":"GigabitEthernet1/0/2","access":{"vlan":20}}
         ]
}'
```
