
Command for upgrade
```shell
ansible-playbook cisco_ios.yml -i inventory -e \
'{
"config_type":"upgrade",
"operation":"upgrade",
"old_fw_version":"17.3.3",
"upgraded_fw_name":"cat9k_iosxe.17.03.04.SPA.bin",
"fw_md5":"89c98b1ed44cf6cb1190eca977edb9a5"
 }'
```