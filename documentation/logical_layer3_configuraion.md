## With SVI (Switched Virtual Interface)
Use the following sample ansible command to create vlan by assigning an ip4 address and ip mask

```shell
ansible-playbook  cisco_ios.yml -i inventory -e '{
"config_type":"LOGICAL_LAYER3",
"operation":"create",
"config":[
            {"name":"Vlan_50","vlan_id":50,"ipv4addr":"10.2.0.1","ip_mask":"255.255.255.0"}
         ]
}'
```

Use the following sample ansible command to create vlan by assigning an ip4 address and ip mask via Curl command
```shell
export var='{"extra_vars": "{
\"config_type\": \"LOGICAL_LAYER3\",
\"operation\": \"create\",
\"config\": [{\"name\":\"Vlan_50\",\"vlan_id\":50,\"ipv4addr\":\"10.2.0.1\",\"ip_mask\":\"255.255.255.0\"}]
}"
}'

echo $var | curl -v -k -u admin:admin -H 'content-type: application/json' -X  POST -d "$(</dev/stdin)" https://172.16.240.138/api/v2/job_templates/14/launch/
```

Use the following sample ansible command to create vlan by assigning an ipv6 and ipv4
```shell
ansible-playbook  cisco_ios.yml -i inventory -e '{
"config_type":"LOGICAL_LAYER3",
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
\"config_type\":\"LOGICAL_LAYER3\",
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

