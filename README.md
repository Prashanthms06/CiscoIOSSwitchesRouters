# Ansible playbooks for Cisco IOS/IOS-XE devices


## _Pre-Requisities_
The playbook has been tested on the following version of softwares:

Sr.Num|Features|
|-----------|-------|
|OperatingSystem|RHEL 8.3|
|Python|3.7.5|
|pip3|21.1.2|
|ansible|2.9.20|
|ansible.utils collection| 2.2.0|
|jsonschema|3.2.0|
|ansible.netcommon|2.2.0|
|Cisco IOS collections|2.3.0|

### Setting up the environment (With internet)

Run the following commands on every ansible controller machine and on the isoloated nodes, if any.
```sh
pip3 install jsonschema==3.2.0
```

Install the ansible collections in the following order
```shell
cd <PROJECT_ROOT_FOLDER>
cp downloads/ansible-utils-2.2.0.tar.gz .
ansible-galaxy collection install ansible-utils-2.2.0.tar.gz -p collections

cp downloads/ansible-netcommon-2.2.0.tar.gz .
ansible-galaxy collection install ansible-netcommon-2.2.0.tar.gz -p collections

cp downloads/cisco-ios-2.3.0.tar.gz .
ansible-galaxy collection install cisco-ios-2.3.0.tar.gz -p collections

```
### Setting up the environment (Without internet)
Refer [Offline Setup](documentation/offline_setup.md)

Install the ansible collections in the following order
```shell
cd <PROJECT_ROOT_FOLDER>
cp downloads/ansible-utils-2.2.0.tar.gz .
ansible-galaxy collection install ansible-utils-2.2.0.tar.gz -p collections

cp downloads/ansible-netcommon-2.2.0.tar.gz .
ansible-galaxy collection install ansible-netcommon-2.2.0.tar.gz -p collections

cp downloads/cisco-ios-2.3.0.tar.gz .
ansible-galaxy collection install cisco-ios-2.3.0.tar.gz -p collections

```

## _Supported Features_

Sr.Num|Features|Description|
|------|--------|-----------|
|1|[SwitchPortConfiguration](documentation/switch_port_configuration.md) | Switch port  related configuration|
|2|[VLANConfiguration](documentation/vlan_configuration.md) | VLAN Configuration|
|3|[ComplianceCheck](documentation/compliance.md) | Compliance check|
|4|[SwitchBaseACL Configuration](documentation/switch_base_acl.md) | ACL configuration|
|5|[PhysicalLayer3Configuration](documentation/physical_layer3_configuration.md) | Physical layer3 configuration|
|4|[LogicalLayer3Configuration ](documentation/logical_layer3_configuration.md) | Logical layer3 configuration|














