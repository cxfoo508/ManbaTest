from data_method import *

# agent_name
parm_001 = [{
    "agent_name": "test-app",
    "agent_detail": "test",
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"agent_id"']
parm_002 = [{
    "agent_name": "测试app",
    "agent_detail": "test",
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"agent_id"']
parm_003 = [{
    "agent_name": "test!@~#$%^& ,.;'",
    "agent_detail": "test",
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"agent_id"']
parm_004 = [{
    "agent_name": "12344",
    "agent_detail": "test",
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"agent_id"']
parm_005 = [{
    "agent_name": "12344",
    "agent_detail": "test",
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"agent_id"']
parm_006 = [{
    "agent_name": get_str(25),
    "agent_detail": "test",
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
},
    '[{"loc":["body","agent_name"],"msg":"ensure this value has at most 32 characters","type":"value_error.any_str.max_length","ctx":{"limit_value":32}}]'
]
parm_006_1 = [{
    "agent_name": get_str(24),
    "agent_detail": "test",
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"agent_id"']
parm_006_2 = [{
    "agent_name": get_str(99),
    "agent_detail": "test",
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
},
    '[{"loc":["body","agent_name"],"msg":"ensure this value has at most 32 characters","type":"value_error.any_str.max_length","ctx":{"limit_value":32}}]'
]
parm_007 = [{
    "agent_detail": "test",
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
}, '']
# agent_ditail
parm_008 = [{
    "agent_name": "test-app",
    "agent_detail": "总问字符",
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"agent_id"']
parm_009 = [{
    "agent_name": "test-app",
    "agent_detail": "test～！@#¥%……&*，。 ",
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"agent_id"']
parm_010 = [{
    "agent_name": "test-app",
    "agent_detail": get_str(512),
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"agent_id"']
parm_010_1 = [{
    "agent_name": "test-app",
    "agent_detail": get_str(513),
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
},
    '[{"loc":["body","agent_detail"],"msg":"ensure this value has at most 512 characters","type":"value_error.any_str.max_length","ctx":{"limit_value":512}}]']

parm_011 = [{
    "agent_name": "test-app",
    "agent_detail": "测试",
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"agent_id"']

parm_012 = [{
    "agent_name": "test-app",
    "agent_detail": "测试!@~#$%^&*<>, ?",
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"agent_id"']

parm_014 = [{
    "agent_name": "test-app",
    "agent_logo": "data/科比.jpeg",
    "lang": "zh-CN"
}, '']

# agent_logo
parm_015 = [{
    "agent_name": "test-app",
    "agent_detail": "测试",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"agent_id"']
parm_016 = [{
    "agent_name": "test-app",
    "agent_detail": "测试",
    "agent_logo": "12312334!@#$%^ ,.",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"agent_id"']
parm_017 = [{
    "agent_name": "test-app",
    "agent_detail": "测试",
    "agent_logo": "data/科比.jpeg",
    "lang": "en-US"
}, '{"code":0,"msg":"","data":{"agent_id"']
parm_018 = [{
    "agent_name": "test-app",
    "agent_detail": "测试",
    "agent_logo": "data/科比.jpeg",
    "lang": "esdfsdag善良的看法离开的肌肤"
}, '"msg":"ensure this value has at most 10 characters","type":"value_error.any_str.max_length","ctx":{"limit_value":10}}]}']

parm_list = dir()


def get_parms_list_01(parm_name=None):
    lists = []
    if parm_name is None:
        [lists.append(item) for item in parm_list if "parm" in item]
    else:
        for item in parm_list:
            if item == parm_name:
                lists.append(item)
    return lists



