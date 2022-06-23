from data_method import *
# entity_name
parm_entity_001 = [{
        "agent_id": "409",
        "entity_name": get_str(4),
        "entity_type": 1
    }, '{"code":0,"msg":"","data":{"entity_id"']
parm_entity_002 = [{
    "agent_id": "409",
    "entity_name": f"{get_str(4)}1234asdaSD",
    "entity_type": 1
}, '{"code":0,"msg":"","data":{"entity_id"'
]
parm_entity_003 = [{
    "agent_id": "409",
    "entity_name": get_str(4) + "~!@# $%^",
    "entity_type": 1
}, '{"code":0,"msg":"","data":{"entity_id"']
parm_entity_004 = [{

    "entity_name": get_str(4),
    "entity_type": 1}
    ,'[{"loc":["body","agent_id"],"msg":"field required","type":"value_error.missing"}]']
parm_entity_005 = [{
    "agent_id": "409",

    "entity_type": 1
}, '[{"loc":["body","entity_name"],"msg":"field required","type":"value_error.missing"}]']
parm_entity_006 = [{
    "agent_id": "409",
    "entity_name": get_str(4)

}, '[{"loc":["body","entity_type"],"msg":"field required","type":"value_error.missing"}]']

parm_list = dir()


def get_create_entity_list(parm_name=None):
    lists = []
    if parm_name is None:
        [lists.append(item) for item in parm_list if "parm_entity" in item]
    else:
        for item in parm_list:
            if item == parm_name:
                lists.append(item)
    return lists