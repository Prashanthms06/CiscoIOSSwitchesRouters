# Ansible playbooks for Cisco IOS/IOS-XE devices

## Setting up the environment 

Install the ansible collections in the following order
```shell
cp downloads/ansible-utils-2.2.0.tar.gz .
ansible-galaxy collection install ansible-utils-2.2.0.tar.gz -p collections

cp downloads/ansible-netcommon-2.2.0.tar.gz .
ansible-galaxy collection install ansible-netcommon-2.2.0.tar.gz -p collections

cp downloads/cisco-ios-2.3.0.tar.gz .
ansible-galaxy collection install cisco-ios-2.3.0.tar.gz -p collections

```

## Switch port configuration 

Command to assign a port to a vlan in an access mode
```shell
ansible-playbook cisco_ios.yml -i inventory -e '{"operation_type":"switch_port_configuration","config":[{"name":"GigabitEthernet1/0/2","access":{"vlan":20}}]}'
```











