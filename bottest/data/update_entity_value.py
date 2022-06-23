# entity_name
update_entity_value_001 = [{
    "agent_id": "409",
    "entity_id": "",
    "entity_value_id": "",
    "entity_type": 1,
    "value": "测试更新value",
    "phrases": "string",
    "replacetext": "string"
}, '{"code":0,"msg":"","data":{"agent_id"']

parm_list = dir()


def get_parms_list(parm_name=None):
    lists = []
    if parm_name is None:
        [lists.append(item) for item in parm_list if "parm_entity" in item]
    else:
        for item in parm_list:
            if item == parm_name:
                lists.append(item)
    return lists


if __name__ == '__main__':
    a = get_parms_list("parm_001")
    print(a)
