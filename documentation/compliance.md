
Run the following sample command to check the compliance
```shell
ansible-playbook cisco_ios.yml -i inventory -e \
'{
"config_type":"audit",
"operation":"audit"
}' --check --diff
```