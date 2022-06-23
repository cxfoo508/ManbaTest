import copy

import pytest

from bottest.base_case import *
from bottest.data.data_method import *
from bottest.modules.method import method_class


class PyBase_v2:
    get_str = get_str(0)

    @staticmethod
    def run_v2(creat_data):
        """
        执行case
        """
        flow_name = ""
        if "name" in dict(creat_data).keys():
            flow_name = creat_data["name"]
        for i in creat_data['sort']:
            # 深度拷贝数据来进行操作，不影响原数据
            i = copy.deepcopy(i)
            req = i['data']
            lable = f"{flow_name}.{i['lable']}"
            functionClass = i["functionClass"]
            function = i['function']
            assert_param = i['assert']
            environ = i['environ']
            method = i['method']
            log.info(f"RUN DARA CASE:============{lable}============\n")

            # 替换data生成字段get_str get_int envrion get_uuid
            update_dict(req)

            # 引用类
            if '.' in functionClass:
                class_list = functionClass.split('.')
                class_path = functionClass[:functionClass.rindex('.')]
                class_modoul_path = class_list[len(class_list) - 2]
                class_name = class_list[len(class_list) - 1]
                temp = __import__(class_path, fromlist=[class_modoul_path])
                function_class = getattr(temp, class_name)
            else:
                function_class = __import__(functionClass)

            try:
                # 执行function
                res_json = eval(f'function_class.{function}({req})')
                os.environ["res_environ"] = res_json
                res = json.loads(res_json)

                # 注入项
                for k, v in environ.items():
                    if '$' not in v:
                        os.environ[k] = str(eval(v))
                        log.info(f"ENVIRON {k}={v}:{k}={eval(v)}")
                    else:
                        set_environ(k, v, res, req)

                # 断言
                for s in assert_param:
                    # 判断断言版本
                    assert_v = type(s)
                    if assert_v == list:
                        assert_v2(s, res, req, lable)
                    else:
                        assert_v1(s, res, req, lable)

                # 执行功能
                if len(method.keys()) > 0:
                    for k, v in method.items():
                        if k == 'sleep_time':
                            log.info(f'SLEEP_TIME:{v}')
                            time.sleep(v)
            except BaseException as e:
                log.error(f'CODE ERROR:{e}')
                pytest.assume(1 == 2, f"RUN_DATA_CASE: {lable} Error Code:{e}")


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
            assert eval(
                s), f"验证错误:RUN_DATA_CASE: {case_num}\nSELECTOR PARAM: {eval(s_list[0])}\nCHECK PARAM: {eval(s_list[1])} \nRES DARA: {res}"
        else:
            pytest.assume(eval(s),
                          f"验证错误:RUN_DATA_CASE: {case_num}\nSELECTOR PARAM: {eval(s_list[0])}\nCHECK PARAM: {eval(s_list[1])} \nRES DARA: {res}")
    else:
        log.info(f"KEY不存在:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
        if assert_type == 'False':
            assert 1 == 2, f"KEY不存在:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}"
        else:
            pytest.assume(1 == 2, f"KEY不存在:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")


def assert_v2(s, res, req, case_num):
    """
    v2版本断言
    示例：responses:"res-$.xxx.xxx=='xxx'"
         request: "req-$.xxx.xxx=='xxx'"
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
        pytest.assume(check_answer == true_answer, f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
    elif s[1] == '!=':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer != true_answer}')
        pytest.assume(check_answer != true_answer, f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
    elif s[1] == '>=':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer >= true_answer}')
        pytest.assume(check_answer >= true_answer, f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
    elif s[1] == '<=':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer <= true_answer}')
        pytest.assume(check_answer <= true_answer, f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
    elif s[1] == 'in':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer in true_answer}')
        pytest.assume(check_answer in true_answer, f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
    elif s[1] == 'not in':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer not in true_answer}')
        pytest.assume(check_answer not in true_answer,
                      f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
    elif s[1] == 'is':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer is true_answer}')
        pytest.assume(check_answer is true_answer, f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
    elif s[1] == 'is not':
        log.info(f'ASSERT: {assert_str}, ANSWER: {check_answer is not true_answer}')
        pytest.assume(check_answer is not true_answer,
                      f"验证错误:RUN_DATA_CASE: {case_num}\nCHECK PARAM: {s},RES DARA: {res}")
