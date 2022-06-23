from data_method import *

# entity_name
parm_entity_value_list_001 = [{
    "agent_id": "409",
    "entity_id":'',
    "entity_type": 1,
    "entity_value_id":"",
    "page_no":1,
    'number_per_page':10
}, '{"code":0,"msg":"","data":{"rowcount":1}}']
parm_entity_value_list_002 = [{
    "entity_id":'',
    "entity_type": 1,
    "entity_value_id":"",
    "page_no":1,
    'number_per_page':10
}, '[{"loc":["body","agent_id"],"msg":"field required","type":"value_error.missing"}]']
parm_entity_value_list_003 = [{
    "agent_id": "409",
    "entity_type": 1,
    "entity_value_id":"",
    "page_no":1,
    'number_per_page':10
}, '[{"loc":["body","entity_id"],"msg":"field required","type":"value_error.missing"}]']

parm_entity_value_list_004 = [{
    "agent_id": "409",
    "entity_id":'',
    "entity_value_id":"",
    "page_no":1,
    'number_per_page':10
}, '[{"loc":["body","entity_type"],"msg":"field required","type":"value_error.missing"}]']

parm_list = dir()


def get_entity_value_list_data(parm_name=None):
    lists = []
    if parm_name is None:
        [lists.append(item) for item in parm_list if "parm_entity_value_list" in item]
    else:
        for item in parm_list:
            if item == parm_name:
                lists.append(item)
    return lists
