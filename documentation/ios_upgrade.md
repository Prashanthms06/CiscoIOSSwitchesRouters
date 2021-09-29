
Command for upgrade
```shell
ansible-playbook cisco_ios.yml -i inventory -e \
'{
"config_type":"upgrade",
"operation":"upgrade",
"old_fw_version":"17.3.3",
"upgraded_fw_name":"cat9k_iosxe.17.03.04.SPA.bin"
"fw_md5":"0f369ed9e98756f179d4f29d6e7755d3"
 }'
```