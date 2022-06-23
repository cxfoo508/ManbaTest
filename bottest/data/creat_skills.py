from data_method import *


class create_skills_parm:
    # agent_name
    parm_001 = [{
        "agent_id": 0,
        "category_id": 4,
        "intent_id": 0,
        "skill_type": 1,
        "skill_content": {
            "skill_name": get_str(4),
            "description": "描述"
        }
    }, '{"code":0,"msg":"","data":{"agent_id"']
    parm_002 = [{
        "agent_id": 0,
        "skill_name": get_str(4),
        "intent_id": 1,
        "skill_type": 1,
        "description": "string"
    }, '{"code":0,"msg":"","data":{"agent_id"']
    parm_003 = [{
        "agent_id": 0,
        "skill_name": get_str(4),
        "intent_id": 1,
        "skill_type": 2,
        "description": "string"
    }, '{"code":0,"msg":"","data":{"agent_id"']
    parm_004 = [{
        "agent_id": 0,
        "skill_name": get_str(4),
        "intent_id": 1,
        "skill_type": 3,
        "description": "string"
    }, '{"code":0,"msg":"","data":{"agent_id"']

    parm_list = dir()

    @classmethod
    def get_parms_list(cls, parm_name=None):
        lists = []
        if parm_name is None:
            for i in cls.parm_list:
                if "parm" in i:
                    lists.append(eval("cls." + i))
        else:
            for item in cls.parm_list:
                if item == parm_name:
                    lists.append(eval("cls." + item))
        return lists


if __name__ == '__main__':
    b = create_skills_parm.get_parms_list()
    print(b)
