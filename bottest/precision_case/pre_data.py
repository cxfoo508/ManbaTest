import os
import uuid

from bottest.modules.logger import log
import random


class Presicion_intent:
    def __init__(self):
        self.intent_param = [
            {
                "agent_id": os.environ.get('agent_id'),
                "intent_name": "效果测试",
                "examples": [

                ],
                "keywords_eq": [
                ],
                "keywords_include": [
                ]
            },
            ['res["code"]==0', 'res["msg"]=="创建意图成功"'],
            {'intent_id': 'res["data"]["intent_id"]'}
        ]
        self.faq_param = [
            {  # faq
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==0', 'res["msg"] == "创建技能成功"', 'res["data"]["skill_id"]!=None',
                'res["data"]["skill_one_id"]!=None'],
            {'skill_one_id': 'res["data"]["skill_one_id"]',
             'resp_content': 'req["skill_content"]["faq_responses"][0]["resp_content"]',
             'skill_id': 'res["data"]["skill_id"]'
             }]
        self.query_param = [
            {
                "username": str(uuid.uuid4()),
                "msg_body": {
                    "text": {
                        "content": None
                    }
                }
            }, ['res["code"]==0'], {}]
        Line = os.environ.get('line')
        query = os.environ.get('query')
        # 修改意图参数
        if Line is not None:
            line_list = Line.split("	")
            intent_name = str(line_list[0]).replace('\n', '').replace('/', ' or ')
            intent_examples = str(line_list[1]).replace('\n', '').replace('/', ' or ').split('||')
            for i in intent_examples:
                self.intent_param[0]["examples"].append({"id": 0, "name": i})
            self.intent_param[0]["intent_name"] = f"{intent_name}{random.randint(1, 10000)}"
            self.faq_param[0]["skill_content"]["faq_responses"][0][
                "resp_content"] = f"{intent_name}{random.randint(1, 10000)}"
        # 修改query参数
        if query is not None:
            query_list = query.replace('\n', '').strip().replace('/', ' or ').split('	')
            os.environ["query_answer"] = query_list[1].strip().replace('/', ' or ')
            self.query_param[0]["msg_body"]["text"]['content'] = query_list[0]
            log.info(f'CHECK ANSWER:{os.environ.get("query_answer")}')
            assert_res = 'str(res["data"]["responses"][0]["msg_body"]["text"]["content"]).replace(" ","").replace("?Recommended?","[Recommended]").lower() in (str(os.environ.get("query_answer")).replace(" ","").lower()).split("||")'
            self.query_param[1].append(
                assert_res
            )


class precision_data:
    login_params = {
        "sort": ["auth_login"],
        "params": ["node_data_class.param_005"]
    }
    app_params = {
        "sort": ["creat_app"],
        "params": ["node_data_class.param_006_1"]
    }
    app_params_1 = {
        "sort": ["creat_app"],
        "params": ["node_data_class.param_006_2"]
    }
    app_params_2 = {
        "sort": ["creat_app"],
        "params": ["node_data_class.param_006_3"]
    }
    app_params_3 = {
        "sort": ["creat_app"],
        "params": ["node_data_class.param_006_4"]
    }
    app_params_4 = {
        "sort": ["creat_app"],
        "params": ["node_data_class.param_006_5"]
    }
    app_params_5 = {
        "sort": ["creat_app"],
        "params": ["node_data_class.param_006_6"]
    }
    intents_params = {
        "sort": ["create_intent"],
        "params": ["Presicion_intent.intent_param"]
    }
    faq_params = {
        "sort": [
            "skills_base_class.skill_category_all", "skills_base_class.skill_create",
            "skills_base_class.skill_change_status",
        ],
        "params": [
            "skills_data_class.params_case_002", "Presicion_intent.faq_param",
            "skills_data_class.params_case_003_1",
        ]
    }
    agent_publish_params = {
        "sort": ["agent_train_publish_start"],
        "params": ["app_data_class.param_agent_start_pre"]
    }
    query_pre_params = {
        "sort": ["channels_base_class.get_channels_response"],
        "params": ['Presicion_intent.query_param']
    }
