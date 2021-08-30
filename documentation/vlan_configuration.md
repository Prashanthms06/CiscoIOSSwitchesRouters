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
            {"name":"Vlan_100","vlan_id":100}
         ]
 }'
```

Use the following sample ansible command to create a vlan without assigning svi via Curl command
```shell
export var='{"extra_vars" :
"{
\"config_type\":\"vlan_configuration\",
\"operation\":\"create\",
\"config\":[{\"name\":\"Vlan_100\",\"vlan_id\":100}]}"
}'
echo $var | curl -v -k -u admin:admin -H 'content-type: application/json' -X  POST -d "$(</dev/stdin)" https://172.16.240.138/api/v2/job_templates/14/launch/ 
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
```

Use the following sample ansible command to create vlan by assigning an ip4 address and ip mask via Curl command
```shell
export var='{"extra_vars": "{
\"config_type\": \"vlan_configuration\",
\"operation\": \"create\",
\"config\": [{\"name\":\"Vlan_50\",\"vlan_id\":50,\"ipv4addr\":\"10.2.0.1\",\"ip_mask\":\"255.255.255.0\"}]
}"
}'

echo $var | curl -v -k -u admin:admin -H 'content-type: application/json' -X  POST -d "$(</dev/stdin)" https://172.16.240.138/api/v2/job_templates/14/launch/
```

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

Use the following sample ansible command to create vlan by assigning an ipv6 and ipv4 via Curl command
```shell
export var='{"extra_vars" :"{
\"config_type\":\"vlan_configuration\",
\"operation\":\"create\",
\"config\":[{\"name\":\"Vlan_99\",
                \"vlan_id\":99,
                \"ipv4addr\":\"10.6.0.1\",
                \"ip_mask\":\"255.255.255.0\",
                \"ipv6addr\":\"2001:df3:bf80:4285:10:152:120:222/64\",
                \"description\": \"Creating via ansible tower\"
}]
}"
}'
echo $var | curl -v -k -u admin:admin -H 'content-type: application/json' -X  POST -d "$(</dev/stdin)" https://172.16.240.138/api/v2/job_templates/14/launch/
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
