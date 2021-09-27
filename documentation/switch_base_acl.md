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

Command to switch base acl deletion in standard mode when delete all is yes


```shell
ansible-playbook cisco_ios.yml -i hosts -e \
'{
"config_type":"acl",
"operation":"DELETE",
"acl_num":"1",
"delete_all":"yes"
}'
```


Command to switch base acl deletion in standard mode when delete all is no


```shell
ansible-playbook cisco_ios.yml -i hosts -e \
'{
"config_type":"acl",
"operation":"DELETE",
"acl_num":"1",
"delete_all":"no",
"grant": "deny",
"source": "20.10.1.1",
"src_mask_bits": "0.0.0.255",
"interface": "GigabitEthernet1/0/2",
"direction" : "in"
}'
```

Command to switch base acl deletion in extended mode when delete all is yes

````shell
ansible-playbook cisco_ios.yml -i hosts -e \
'{
"config_type":"acl",
"operation":"DELETE",
"acl_num":"TestACL",
"deletion":"yes",

}'
````

Command to switch base acl deletion in extended mode when delete all is no

````shell
ansible-playbook cisco_ios.yml -i hosts -e \
'{
"config_type":"acl",
"operation":"DELETE",
"acl_num":"TestACL",
"deletion":"no",
"grant": "permit",
"source": "1.1.1.1",
"src_mask_bits": "0.0.0.255",
"destination": "3.2.2.2",
"dest_mask_bits": "0.0.0.255",
"dest_ports": [
{
"port_type": "udp",
"port_num": 25
}
],
"interface": "Gigabitethernet1/0/1",
"direction": "out"
}'
````