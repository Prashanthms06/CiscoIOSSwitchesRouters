Sample command to create vlan tags

```shell
ansible-playbook cisco_fmc.yml -i inventory_local -e \
'{
    "object_type":"VlanTags",
    "operation":"post",
    "fmc_host" : 10.10.20.40,
    "username" : user,
    "password": user,
    "req_body":
              {
                 "type": "VlabTag",
                 "overridable": false,
                 "name": "OnenewVlanTag99",
                 "description": "New VlanTag test",
                  "data": {
                        "startTag": 1,
                        "endTag": 3
                          }
              }
}'
```