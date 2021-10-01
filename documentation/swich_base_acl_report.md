## ACL Creation
Example

Command to get acl report when sending reports through email is not required

```shell
  ansible-playbook cisco_ios.yml -i hosts -e \
'{
"config_type":"acl",
"operation":"get",
"send_email":"no",
"zip_passwd":"1qaz2wsx",
"acl_list": [
"1","TestACL"
]
}'
```

Command to get acl report and send them through email 

```shell
  ansible-playbook cisco_ios.yml -i hosts -e \
'{
"config_type":"acl",
"operation":"get",
"send_email":"yes",
"to_mail_id":"pras@ansible-srv",
"smtp_srv":"smtp-server-name",
"smtp_user":"user",
"smtp_user_passwd":"password",
"zip_passwd":"1qaz2wsx",
"acl_list": [
"1","TestACL"
]
}'
```