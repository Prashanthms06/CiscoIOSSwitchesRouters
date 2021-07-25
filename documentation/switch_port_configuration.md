[Main Menu](../README.md)
# Switch port configuration 
Command to assign a port to a vlan in an access mode
```shell
ansible-playbook cisco_ios.yml -i inventory -e '{"config_type":"switch_port_configuration","operation_type":"create","config":[{"name":"GigabitEthernet1/0/2","access":{"vlan":20}}]}'
```
