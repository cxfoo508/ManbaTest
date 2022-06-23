from data_method import *

# entity_name
parm_update_entity_001 = [{
    "entity_id":"",
    "agent_id": "409",
    "entity_name": get_str(4),
    "entity_type": 1
}, '{"code":0,"msg":"","data":{"rowcount":1}}']

parm_update_entity_002 = [{
    "entity_id":"",
    "agent_id": "409",
    "entity_name": get_str(4)+"123sddsfsd",
    "entity_type": 1
}, '{"code":0,"msg":"","data":{"rowcount":1}}']
parm_update_entity_003 = [{
    "entity_id":"",
    "agent_id": "409",
    "entity_name": get_str(4)+"~!@  # d$",
    "entity_type": 1
}, '{"code":0,"msg":"","data":{"rowcount":1}}']
parm_update_entity_004 = [{
    "entity_id":"",
    "entity_name": get_str(4),
    "entity_type": 1
}, '[{"loc":["body","agent_id"],"msg":"field required","type":"value_error.missing"}]']
parm_update_entity_005 = [{
    "entity_id":"",
    "agent_id": "409",
    "entity_type": 1
}, '[{"loc":["body","entity_name"],"msg":"field required","type":"value_error.missing"}]']
parm_update_entity_006 = [{
    "entity_id":"",
    "agent_id": "409",
    "entity_name": get_str(4),
}, '[{"loc":["body","entity_type"],"msg":"field required","type":"value_error.missing"}]']
parm_update_entity_007 = [{
    "agent_id": "409",
    "entity_name": get_str(4),
    "entity_type": 1
}, '[{"loc":["body","entity_id"],"msg":"field required","type":"value_error.missing"}]']

parm_list = dir()


def get_update_entity_list(parm_name=None):
    lists = []
    if parm_name is None:
        [lists.append(item) for item in parm_list if "parm_update_entity" in item]
    else:
        for item in parm_list:
            if item == parm_name:
                lists.append(item)
    return lists
