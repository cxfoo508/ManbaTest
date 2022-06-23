from data_method import *

# agent_name
up_parm_001 = [{
    "agent_name": "test-app",
    "agent_detail": "test",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"rowcount":1}}']
up_parm_002 = [{
    "agent_name": "测试app",
    "agent_detail": "test",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"rowcount":1}}']
up_parm_003 = [{
    "agent_name": "test!@~#$%^& ,.;'",
    "agent_detail": "test",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"rowcount":1}}']
up_parm_004 = [{
    "agent_name": "12344",
    "agent_detail": "test",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"rowcount":1}}']
up_parm_005 = [{
    "agent_name": "12344",
    "agent_detail": "test",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"rowcount":1}}']
up_parm_006 = [{
    "agent_name": "wrtwrtwrtwrtwrtwrtwrtwrtwrtwrtwrt中打开房间数量大幅减少代理费中打开房间数量大幅减少代理费中打开房间数量大幅减少代理费中打开房间数量大幅减少代理费中打开房间数量大幅减少代理费",
    "agent_detail": "test",
    "lang": "zh-CN"
},
    '[{"loc":["body","agent_name"],"msg":"ensure this value has at most 32 characters","type":"value_error.any_str.max_length","ctx":{"limit_value":32}}]']

up_parm_006_1 = [{
    "agent_name": get_str(32),
    "agent_detail": "test",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"rowcount":1}}']
up_parm_007 = [{
    "agent_detail": "test",
    "lang": "zh-CN"
}, '[{"loc":["body","agent_name"],"msg":"field required","type":"value_error.missing"}]']
# agent_ditail
up_parm_008 = [{
    "agent_name": "test-app",
    "agent_detail": "总问字符",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"rowcount":1}}']
up_parm_009 = [{
    "agent_name": "test-app",
    "agent_detail": "test～！@#¥%……&*，。 ",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"rowcount":1}}']
up_parm_010 = [{
    "agent_name": "test-app",
    "agent_detail": "短发短发的股份公司的分公司奉公守法故事风格发反反复复反反复复反反复复反反复复反反复复哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥哥发反反复复发反反复复反反复复反反复复哥哥哥哥哥哥过",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"rowcount":1}}']

up_parm_011 = [{
    "agent_name": "test-app",
    "agent_detail": "测试",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"rowcount":1}}']

up_parm_012 = [{
    "agent_name": "test-app",
    "agent_detail": "测试!@~#$%^&*<>, ?",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"rowcount":1}}']
up_parm_013 = [{
    "agent_name": "test-app",
    "agent_detail": "a收到发生的点点滴滴大大方方反反复复反反复复看坎坎坷坷坎坎坷坷坎坎坷坷看了零零落落零零落落零零落落滴滴答答滴滴答答反反复复方法",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"rowcount":1}}']

up_parm_014 = [{
    "agent_name": "test-app",
    "lang": "zh-CN"
}, '']

up_parm_015 = [{
    "agent_name": "test-app",
    "agent_detail": "测试",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"rowcount":1}}']
up_parm_016 = [{
    "agent_name": "test-app",
    "agent_detail": "测试",
    "lang": "zh-CN"
}, '{"code":0,"msg":"","data":{"rowcount":1}}']
up_parm_017 = [{
    "agent_name": "test-app",
    "agent_detail": "测试",
    "lang": "en-US"

}, '{"code":0,"msg":"","data":{"rowcount":1}}']
up_parm_018 = [{
    "agent_name": "test-app",
    "agent_detail": "测试",
    "lang": "esdfsdag善良的看法离开的肌肤"
}, '{"code":422,"msg":"parameter invalid","data":[{"loc":["body","lang"],"msg":"ensure this value has at most 10 characters","type":"value_error.any_str.max_length","ctx":{"limit_value":10}}]}']

up_parm_list = dir()


def get_update_list(parm_name=None):
    lists = []
    if parm_name is None:
        [lists.append(item) for item in up_parm_list if "up_parm" in item]
    else:
        for item in up_parm_list:
            if item == parm_name:
                lists.append(item)
    return lists


# if __name__ == '__main__':
#     lists = get_update_list("up_parm_001")
#     print(lists)
