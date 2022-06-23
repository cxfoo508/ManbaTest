import ast
import datetime
import uuid

from jsonpath import jsonpath

from bottest.modules.logger import log

class method_class:
    @classmethod
    def get_node_list(cls, param_list, parm_name=None):
        lists = []
        if parm_name is None:
            for i in param_list:
                if "case" in i:
                    lists.append(i)
        else:
            for item in param_list:
                if parm_name in item:
                    lists.append(item)
        return lists

    @classmethod
    def param_exist(cls, param, res):
        """
        判断字典是否包含key
        """
        type_assert = ['==', '!=', '<=', '>=', ' is ', ' in ', '>', '<']
        for i in type_assert:
            if i in param:
                param = (str(param).split(i))[0].strip()
                break
        try:
            if 'res' in param:
                eval(param)
                return True
            else:
                return True
        except Exception as err:
            log.error(f'key:{param}不存在{err}')
            return False

    @classmethod
    def get_time_param(cls, num=-1):
        """
        获取距离now的时间段
        """
        UTC_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
        time_now = datetime.datetime.now()
        time_1 = time_now.strftime(UTC_FORMAT)

        # 减少天数
        time_2 = (time_now + datetime.timedelta(days=num)).strftime(UTC_FORMAT)
        return [time_2, time_1]

    @classmethod
    def get_uuid(cls):
        """
        uuid
        """
        uid = uuid.uuid4()
        return str(uid).replace('-', '')

    @classmethod
    def filter_dict(cls, rule, res):
        """
        过滤map
        """
        rules = rule.split('.')
        for r in range(1, len(rules)):
            try:
                key = int(rules[r])
            except Exception as e:
                del e
                key = rules[r]
            finally:
                res = cls.__get_param(key, res)
        return res

    @classmethod
    def __get_param(cls, key, res):
        """
        获取dict和list对象
        """
        param_type = type(res)
        if param_type == dict:
            return res[key]
        elif param_type == list:
            if type(key) == int:
                return res[int(key)]
            elif key == '#':
                return len(res)
            else:
                filter_p = key[1:]
                filter_d = ast.literal_eval(filter_p)
                filter_k = list(filter_d.keys())[0]
                filter_v = list(filter_d.values())[0]
                for d in res:
                    for k, v in d.items():
                        if k == filter_k and v == filter_v:
                            return d

    @classmethod
    def json_path_get(cls, check_json, res):
        """
        执行jsonpath
        """
        result = jsonpath(res, check_json)
        return result



if __name__ == '__main__':
    print(method_class.get_time_param())
