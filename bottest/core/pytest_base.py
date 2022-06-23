# <editor-fold desc = "import">
import pytest
from bottest.modules.method import method_class
from case.test_app.app_sort_data import app_sort_class
from case.test_app.app_data import app_data_class
from case.test_intents.intents_base import intents_base_class
from case.test_intents.intents_data import intents_data_class
from case.test_intents.inrents_sort_data import intents_sort_class
from case.test_botfallbackconfig.botfallbackconfig_sort_data import botfallbackconfig_sort_class
from case.test_botfallbackconfig.botfallbackconfig_base import botfallbackconfig_base_class
from case.test_botfallbackconfig.botfallbackconfig_data import botfallbackconfig_data_class
from case.test_botresponse.botreponse_sort_data import botresponse_sort_class
from case.test_botresponse.botresponse_base import botresponse_base_class
from case.test_botresponse.botreponse_data import botreponse_data_class
from case.test_channels.channels_sort_data import channels_sort_class
from case.test_channels.channels_data import channels_data_class
from case.test_channels.channels_base import channels_base_class
from case.test_node.node_data import node_data_class
from case.test_node.node_sort_data import node_sort_class
from case.test_node.node_base import node_base_class
from case.test_entity.entity_sort_data import entity_sort_class
from case.test_entity.entity_data import entity_data_class
from case.test_channels_new.channels_base import channels_base_new_class
from case.test_channels_new.channels_data import channels_data_new_class
from case.test_channels_new.channels_sort_data import channels_sort_new_class
from case.test_skills.skills_data import skills_data_class
from case.test_skills.skills_sort_data import skills_sort_class
from case.test_skills.case_base_skills import skills_base_class
from case.test_chatMessage.message_base import ChatMessageCase
from case.test_entity_new.entity_base import entity_base_new_class
from case.test_entity_new.entity_data import entity_data_new_class
from case.test_entity_new.entity_sort_data import entity_sort_new_class
from case.test_labelquery.labelquery_base import label_query_base_class
from case.test_labelquery.labelquery_data import label_query_data_class
from case.test_labelquery.labelquery_sort_data import label_query_sort_class
from case.test_slot.slot_base import SlotCaseBase
from case.test_slot.slot_data import slot_data_class
from case.test_slot.slot_sort_data import slot_sort_class
from case.test_rule.rule_base import rule_base_class
from case.test_rule.rule_data import rule_data_class
from case.test_rule.rule_sort_data import rule_sort_class
from case.test_skills_new.skills_base_case_new import skills_case_base_new
from case.test_skills_new.skills_data_new import skills_data_new_calss
from case.test_skills_new.skills_sort_data_new import skills_sort_new_class
from case.test_attribute.attribute_base import attribute_base_class
from case.test_attribute.attribute_data import attribute_data_class
from case.test_attribute.attribute_sort_data import attribute_sort_class
from precision_case.pre_data import precision_data
from precision_case.pre_data import Presicion_intent
from case.test_BackgroundTask.ground_task_sort_data import ground_task_sort_class
from case.test_BackgroundTask.ground_task_case_base import ground_task_base_class
from case.test_BackgroundTask.ground_task_data import ground_task_data_class
from case.test_licenses.licenses_base import licenses_base_class
from case.test_licenses.licenses_sort_data import licenses_sort_class
from case.test_licenses.licenses_data import licenses_data_class
from case.test_permissions.permissions_base import permissions_base_class
from case.test_permissions.permissions_data import permissions_data_class
from case.test_permissions.permissions_sort_data import permissions_sort_class
from case_v1.test_slot_v1.slot_base import SlotCaseBase_v2
from case_v1.test_slot_v1.slot_data import slot_data_class_v2
from case_v1.test_slot_v1.slot_sort_data import slot_sort_class_v2
from case_v1.test_skills_v1.skills_sort_data import skills_sort_class_v2
from case_v1.test_skills_v1.skills_data import skills_data_class_v2
from case_v1.test_skills_v1.case_base_skills import skills_base_class_v2
from case_v1.test_app_v1.app_case_base import app_base_class
from case_v1.test_entity_v1.entity_base_v1 import entity_base_v1_class
from case_v1.test_entity_v1.entity_data_v1 import entity_data_v1_class
from case_v1.test_entity_v1.entity_sort_data_v1 import entity_sort_v1_class
from case_v1.test_channels_v1.channels_sort_data_v1 import channels_sort_v1_class
from case_v1.test_channels_v1.channels_data_v1 import channels_data_v1_class
from case_v1.test_channels_v1.channels_base_v1 import channels_base_v1_class
from case_v1.test_attribute_v1.attribute_base_v1 import attribute_base_v1_class
from case_v1.test_attribute_v1.attribute_data_v1 import attribute_data_v1_class
from case_v1.test_attribute_v1.attribute_sort_data_v1 import attribute_sort_v1_class
from case_v1.test_skills_block_v1.skills_data_new import skills_data_new_calss_v1
from case_v1.test_skills_block_v1.skills_sort_data_new import skills_sort_new_class_v1
from base_case import *
import os
import ast
# </editor-fold>


class PyBase:

    @staticmethod
    def run(creat_data):
        """
        执行case
        """
        data = eval(creat_data)
        log.info(f'RUN SORT CASE: <<<<<<<<<<<<<<<<{creat_data}<<<<<<<<<<<<<<<<\n\n')
        # 要执行的func和执行顺序
        sort_data = data['sort']
        log.info(sort_data)
        # 参数包含入参，param_data，注入数据
        param_data = data['params']
        log.info(param_data)
        # 遍历并且执行每个func
        for i in range(len(sort_data)):
            # 判断参数类型
            param_type = type(param_data[i])
            object_x = eval(str(param_data[i]).split('.')[0] + '()')
            param_n = str(param_data[i]).split('.')[1]
            param = eval('object_x.' + param_n)
            func = sort_data[i]
            req = param[0]
            try:
                # 执行func
                log.info(f"RUN DARA CASE:============{param_data[i]}============\n")
                res_json = eval(f'{func}({req})')
                os.environ["res_environ"] = res_json
                res = json.loads(res_json)
                # res注入项
                for k, v in param[2].items():
                    if '$' not in v:
                        os.environ[k] = str(eval(v))
                        log.info(f"ENVIRON {k}={v}:{k}={eval(v)}")
                    else:
                        set_environ(k, v, res, req)
                # assert
                for s in param[1]:
                    # 判断断言版本
                    assert_v = type(s)
                    if assert_v == list:
                        assert_v2(s, res, req, param_data[i])
                    else:
                        assert_v1(s, res, req, param_data[i])
                # 执行功能
                if len(param) == 4:
                    for k, v in param[3].items():
                        if k == 'sleep_time':
                            log.info(f'SLEEP_TIME:{v}')
                            time.sleep(v)
            except BaseException as e:
                log.error(f'CODE ERROR:{e}')
                pytest.assume(1 == 2, f"RUN_DATA_CASE: {param_data[i]} Error Code:{e}")


def set_environ(k, v, res, req=None):
    """
    注入环境变量
    """
    if 'req' in v:
        res = req
    value = method_class.json_path_get((v.split('-'))[1], res)
    value = [str(i) for i in value]
    value = ','.join(value)
    os.environ[k] = value
    log.info(f"ENVIRON {k}={v}:{k}={value}")


def assert_v1(s, res, req, case_num):
    """
    v1版本断言
    """
    s_list = None
    req = req
    res_json = json.dumps(res, ensure_ascii=False)
    # 判断是否错误终止：
    assert_type = os.environ.get('assert_type')
    # param_exist = True
    param_exist = method_class.param_exist(s, res)
    if param_exist:
        log.info(f'ASSERT: {s},ANSWER:{eval(s)}')
        for i in ['==', '!=', '>=', '<=', '>', '<', ' is not ', ' is ', ' not in ', ' in ']:
            if i in str(s):
                s_list = str(s).split(i)
                break
        if assert_type == 'False':
            assert eval(s), f"验证错误:RUN_DATA_CASE: {case_num}\nSELECTOR PARAM: {eval(s_list[0])}\nCHECK PARAM: {eval(s_list[1])} \nRES DARA: {res}"
        else:
            pytest.assume(eval(s), f"验证错误:RUN_DATA_CASE: {case_num}\nSELECTOR PARAM: {eval(s_list[0])}\nCHECK PARAM: {eval(s_list[1])} \nRES DARA: {res}")
    else:
        log.info(f"KEY不存在:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
        if assert_type == 'False':
            assert 1 == 2, f"KEY不存在:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}"
        else:
            pytest.assume(1 == 2,  f"KEY不存在:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")


def assert_v2(s, res, req, case_num):
    """
    v2版本断言
    示例：responses:["res-$.xxx.xxx", ==, xxx]
         request: ["req-$.xxx.xxx", ==, xxx]
    """
    check_answer = method_class.json_path_get((s[0].split('-'))[1], res)
    check_answer = str(check_answer[0])
    if 'req-' in str(s[2]):
        true_answer = method_class.json_path_get((s[2].split('-'))[1], req)
        true_answer = str(true_answer[0])
    else:
        true_answer = str(s[2])
    assert_str = f'{check_answer}{s[1]}"{true_answer}"'
    if s[1] == '==':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer == true_answer}')
        pytest.assume(check_answer == true_answer,  f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
    elif s[1] == '!=':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer != true_answer}')
        pytest.assume(check_answer != true_answer,  f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
    elif s[1] == '>=':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer >= true_answer}')
        pytest.assume(check_answer >= true_answer,  f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
    elif s[1] == '<=':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer <= true_answer}')
        pytest.assume(check_answer <= true_answer, f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
    elif s[1] == 'in':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer in true_answer}')
        pytest.assume(check_answer in true_answer, f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
    elif s[1] == 'not in':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer not in true_answer}')
        pytest.assume(check_answer not in true_answer, f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
    elif s[1] == 'is':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer is true_answer}')
        pytest.assume(check_answer is true_answer,  f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
    elif s[1] == 'is not':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer is not true_answer}')
        pytest.assume(check_answer is not true_answer, f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")

