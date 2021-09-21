[Main Menu](../README.md)
# Switch Base ACL Configuration

Command to switch base acl in standard mode

```shell
ansible-playbook cisco_ios.yml -i inventory -e \
'{
"config_type":"acl",
"operation":"create",
"acl_num":"1",
"source": "1.1.1.1",
"src_mask_bits": "0.0.0.255",
"grant": "deny",
"interface": "GigabitEthernet1/0/2",
"direction" : "in"
}'
```

Command to switch base acl in extended mode

```shell
ansible-playbook cisco_ios.yml -i inventory -e \
'{
"config_type":"acl",
"operation":"create",
"acl_num":"NamedACL",
"source": "1.1.1.1",
"src_mask_bits": "0.0.0.255",
"grant": "deny",
"interface": "GigabitEthernet1/0/2",
"direction" : "in",
"destination": "2.2.2.2",
"dest_mask_bits":"0.0.255.255",
"dest_ports":[
  {
    "port_type":"udp",
    "port_num":20
  },
  {
    "port_type":"tcp",
    "port_num": 54
  }
]
}'
```