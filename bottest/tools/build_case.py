"""
自动生成单元测试用例
1、根据传入dict转换json schema
2、填写schema中的参数
3、根据填写玩的schema生成单元测试用例和模块文件
"""
import copy
import json

from bottest.modules.helper import *

schema = {
    "title": "data info",
    "type": "object",
    "properties": {},
    "REQUIRED": {}
}


def create_json_schema(json_data, schema_p=schema['properties']):
    """
    字典转换json_schema
    """
    # a = method_class.json_path_get('$.type', schema)
    schema_type = {
        "str": {
            "type": "string",
            "minLength": 3,
            "maxLength": 30,
            "ENUM": [],
            "CONST": ''
        },
        "int": {
            'type': 'number',
            'maximum': 0,
            'minimum': 0,
            "ENUM": [],
            "CONST": ''
        },
        "dict": {
            "type": "object",
            "properties": {},
            "REQUIRED": {},
        },
        "list": {
            "type": "array",
            "items": [],
            "minItems": 0,
            "maxItems": 0
        }
    }
    if type(json_data) == dict:
        for key in json_data.keys():
            key_type = str(type(json_data[key])).split(' ')[1][1:-2]
            schema_value = copy.deepcopy(schema_type[key_type])
            schema_p[key] = schema_value
            if key_type == 'dict':
                create_json_schema(json_data[key], schema_p[key]['properties'])
            elif key_type == 'list':
                items = schema_p[key]['items']
                create_json_schema(json_data[key], items)
    elif type(json_data) == list:
        for i in range(len(json_data)):
            key_type = str(type(json_data[i])).split(' ')[1][1:-2]
            schema_value = copy.deepcopy(schema_type[key_type])
            schema_p.append(schema_value)
            if key_type == 'dict':
                create_json_schema(json_data[i], schema_p[i]['properties'])
            elif key_type == 'list':
                create_json_schema(json_data[i], schema_p[i]['items'])
    with open('json_schema.py', 'w') as file:
        file.write(f'# 请填写：默认值const，必填项required，字段长度，最大值最小值，list长度。---这一行字不能删除\n{json.dumps(schema)}')


def create_case_file(test_name):
    """
    生成case固定文件
    """
    path = os.path.join(file_path(), 'case')
    dir_name = f'{path}/test_{test_name}'
    data_name = f'{dir_name}/{test_name}_data.py'
    sort_name = f'{dir_name}/{test_name}_sort_data.py'
    case_name = f'{dir_name}/test_{test_name}.py'

    # 创建文件夹和文件
    if os.path.exists(dir_name):
        print('文件夹已存在！！！')
    else:
        os.mkdir(dir_name)
        os.system('touch ' + '{' + data_name + ',' + sort_name + ',' + case_name + '}')

        # 写入testcase文件
        case_data = '# coding = utf-8\nimport pytest\nfrom case.pytest_base_t import PyBase\n' \
                    'from case.test_app_t.app_sort_data import app_sort_class\ndef get_by_data()' \
                    ':\n    return app_sort_class.get_list()\nclass TestCase(PyBase):\n    @pytest.' \
                    'fixture(params=get_by_data())\n    def creat_data(self, request):\n        ' \
                    'return request.param\n    def test_001(self, creat_data):\n        ' \
                    'self.run(creat_data)\n'
        with open(case_name, 'w') as file:
            file.write(case_data)

        # 写入sor data文件
        sort_content = 'from case.test_app_t.app_data import *\nfrom data.data_method import *\n' \
                       'class app_sort_class:\n      test_case_001 = {"sort": [param_001]}\n' \
                       '      dir_list = dir()\n      @classmethod\n      def get_list(cls):\n       ' \
                       ' return get_param_list_v2(cls.dir_list, cls)'
        with open(sort_name, 'w') as file:
            file.write(sort_content)

        # 写入data文件


#    0、生成正常参数,是否有枚举值
#    1、string 生成''，' '，None，中英文特殊字符，长度判断
#    2、int 生成 最大值，最小值，负数，范围内值，None，''，' '
#    3、list 生成 长度验证 []
#    4、bool 生成 true false None '' ' '
#    5、dict 必填项 {}
def write_case_const(json_data, schema_p, case_type):
    """
    生成单元测试case
    生成const默认用例
    """

    if type(json_data) == dict:
        for key in json_data.keys():
            key_con = schema_p[key]
            key_type = key_con['type']
            if key_type in ['string', 'number', 'bool']:
                if case_type == 'const':
                    key_const_value = key_con['CONST']
                    if key_const_value != '':
                        json_data[key] = key_const_value
                elif case_type == 'enum':
                    key_const_value = key_con['ENUM']
                    if len(key_const_value) != 0:
                        for v in key_const_value:
                            value_y = json_data[key]
                            json_data[key] = v
                            print(data)
                            json_data[key] = value_y
                            print(data)
            elif key_type == 'object':
                write_case_const(json_data[key], schema_p[key]['properties'], case_type)
            elif key_type == 'array':
                items = schema_p[key]['items']
                write_case_const(json_data[key], items, case_type)
    elif type(json_data) == list:
        for i in range(len(json_data)):
            key_con = schema_p[i]
            key_type = key_con['type']
            if key_type in ['string', 'number', 'bool']:
                if case_type == 'const':
                    key_const_value = key_con['CONST']
                    json_data[i] = key_const_value
                elif case_type == 'enum':
                    key_const_value = key_con['ENUM']
                    if len(key_const_value) != 0:
                        for v in key_const_value:
                            value_y = json_data[i]
                            json_data[i] = v
                            print(data)
                            json_data[i] = value_y
                            print(data)

            elif key_type == 'object':
                write_case_const(json_data[i], schema_p[i]['properties'], case_type)
            elif key_type == 'array':
                items = schema_p[i]['items']
                write_case_const(json_data[i], items, case_type)
    if type(case_type) == 'const':
        with open('/Users/chengxinfei/Documents/GitHub/BlackManba/case/test_chang_jing/chang_jing_data.py',
                  'w') as file:
            file.write(f'param_case_001 = {str(json_data)}')


def create_case():
    with open('json_schema.py', 'r') as file:
        lines = ''
        reads = file.readlines()
        for i in range(len(reads)):
            if i != 0:
                lines += reads[i]
        a = json.loads(lines)
        schema_p = a['properties']
    write_case_const(data, schema_p, 'const')
    # print(data)
    write_case_const(data, schema_p, 'enum')
    # print(data)


if __name__ == '__main__':
    data = {
        "msg_body": {
            "text": {'a': 1}
        },
        # "msg_body": {
        #     "text": {
        #         "content": [{'a': {'b': 1}}]
        #     }
        # },
        "user_id": "string",
        "extra": "string",
        'msg_list': [
            'string'
        ],
        'msg_list_2': [
            'string', {'b': 2}
        ]

    }
    # data = {
    #     "agent_id": "string",
    #     "skill_one_id": "string",
    #     "node_name": "string",
    #     "node_order": 1,
    #     "trigger_intent_ids": [
    #         "string"
    #     ],
    #     "trigger_slot_value": "string",
    #     "slot_id": "string",
    #     "trigger_entities": [
    #         {
    #             "entity_id": "string",
    #             "entity_value_id": "string",
    #             "entity_type_id": 0,
    #             "entity_value": "string"
    #         }
    #     ],
    #     "slot": "string",
    #     "prompts": {
    #         "name": "string",
    #         "mode_id": 1,
    #         "type_id": 1,
    #         "skill_id": 0,
    #         "status": 1,
    #         "agent_id": 0,
    #         "responses": [
    #             {
    #                 "name": "string",
    #                 "response_once": 0,
    #                 "resp_content": "string",
    #                 "resp_order": 0,
    #                 "resp_type_id": 0,
    #                 "sug_intents": [],
    #                 "custom_action_id": 0,
    #                 "event_id": 0
    #             }
    #         ]
    #     },
    #     "responses": {
    #         "name": "string",
    #         "mode_id": 1,
    #         "type_id": 1,
    #         "skill_id": 0,
    #         "status": 1,
    #         "agent_id": 0,
    #         "responses": [
    #             {
    #                 "name": "string",
    #                 "response_once": 0,
    #                 "resp_content": "string",
    #                 "resp_order": 0,
    #                 "resp_type_id": 0,
    #                 "sug_intents": [],
    #                 "custom_action_id": 0,
    #                 "event_id": 0
    #             }
    #         ]
    #     },
    #     "parent_node_id": "string"
    # }

    # create_json_schema(data)
    create_case_file('dashboard')
    create_case()
