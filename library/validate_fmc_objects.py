from ansible.module_utils.basic import AnsibleModule
import traceback


def main():
    module = AnsibleModule(
        supports_check_mode=True,
         argument_spec=dict(
            fmc_mapping=dict(required=True,type=dict),
            object_type=dict(required=True),
            operation=dict(required=True),
        )
    )


    fmc_mappping = module.params['fmc_mapping']
    object_type = module.params['object_type']
    operation = module.params['operation']


    response = dict(
        changed=False,
        object_type=''
    )
    if object_type in fmc_mappping:
        if operation not in fmc_mappping[object_type]['supported_operations'] :
         module.fail_json( msg="operation {} not supported for object type {}:\n{}".format(operation,object_type, traceback.format_exc()))
        else:
            response["object_type"] = fmc_mappping[object_type]['obj_type']

    else:
      module.fail_json(msg="object_type {} is not a valid FMC object type:\n{}".format(object_type, traceback.format_exc()))

    response["changed"] = True
    module.exit_json(**response)

if __name__ == "__main__":
    main()

