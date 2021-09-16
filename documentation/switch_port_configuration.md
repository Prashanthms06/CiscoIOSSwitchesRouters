[Main Menu](../README.md)
# Switch port configuration 

| Parameters | Mandatory/Optional |Remarks |
| ------ | ---------- |----------|
| config_type | Mandatory | Type of the configuration.For this use case, value of this parameter would be switch_port_configuration |
| operation |Mandatory | Type of the operation. Switch port configuration currently supports only create operation |
| config | Mandatory| Configuration to be used.|

Command to configure a port to a vlan in an access mode

```shell
ansible-playbook cisco_ios.yml -i inventory -e \
'{
"config_type":"switch_port_configuration",
"operation":"create",
"config":[
          {"name":"GigabitEthernet1/0/4","access":{"vlan":100},"description":"Configuring via ansible "}
         ]
}'
```
Command to configure a port to a vlan in an access mode via Curl command

```shell
export var='{"extra_vars" :"{
\"config_type\":\"switch_port_configuration\",
\"operation\":\"create\",
\"config\":[{\"name\":\"GigabitEthernet1/0/4\",\"access\":{\"vlan\":100},\"description\":\"ansible\"}]
}"
}'
echo $var | curl -v -k -u admin:admin -H 'content-type: application/json' -X  POST -d "$(</dev/stdin)" https://172.16.240.138/api/v2/job_templates/14/launch/ 
```


Command to configure a port in the trunk mode

```shell
ansible-playbook cisco_ios.yml -i inventory -e \
'{
"config_type":"switch_port_configuration",
"operation":"create",
"config":[
          {"name":"GigabitEthernet1/0/5","trunk":{"vlan_range":"60-70"},"description":"Configuring in trunk mode "}
         ]
}'

```
Command to configure a port in the trunk mode via Curl command

```shell
export var='{"extra_vars" :"{
\"config_type\":\"switch_port_configuration\",
\"operation\":\"create\",
\"config\":[
          {\"name\":\"GigabitEthernet1/0/5\",\"trunk\":{\"vlan_range\":\"60-70\"},\"description\":\"Configuring in trunk mode \"}
         ]
}"
}'
echo $var | curl -v -k -u admin:admin -H 'content-type: application/json' -X  POST -d "$(</dev/stdin)" https://172.16.240.138/api/v2/job_templates/14/launch/ 
```


ommand to configure a port in the port mapping mode

```shell
ansible-playbook cisco_ios.yml -i inventory -e \
'{
"config_type":"switch_port_configuration",
"operation":"create",
"config":[
          {"name":"GigabitEthernet1/0/5","port_mapping":{"vlan_num":22,port_channel_num: 2},"description":"Configuring port mapping "}
         ]
}'

```


