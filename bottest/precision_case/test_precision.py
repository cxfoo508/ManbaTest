import pytest

from base_case import *
from case.pytest_base import PyBase
from tools.build_module import OperationExcel


def query_skills():
    # file_path = '/Users/chengxinfei/Documents/GitHub/BlackManba/data/QAtestdata/Dior.testdata'
    file_path = '/Users/chengxinfei/Documents/GitHub/BlackManba/data/QAtestdata/Nike.testdata'
    with open(file_path, 'r', errors='ignore') as file:
        lines = file.readlines()
    return lines


def query_excel(start_index):
    """
    excel进行query
    """

    file_path = '/Users/chengxinfei/Documents/GitHub/BlackManba/data/QAtestdata/中华ITTestf.xlsx'
    excel = OperationExcel(excel_path=file_path)
    rows = excel.get_values()
    lists = []
    for i in range(len(rows)):
        if i >= start_index:
            line = f'{rows[i][0]}	{rows[i][1]}'
            lists.append(line)
        # if i >= 5:
        #     break
    return lists


class TestCase(PyBase):

    def create_skills(self, file_path):
        """
        文本创建读取配置
        """
        with open(file_path, 'r', errors='ignore') as file:
            while True:
                Line = file.readline()
                Line = Line.replace('/', ' or ')
                if not Line:
                    break
                else:
                    os.environ["line"] = Line
                    self.run("precision_data.intents_params")
                    self.run("precision_data.faq_params")
        self.run("precision_data.agent_publish_params")

    def create_excel_agent(self, start_index, file_path):
        """
        excel读取配置
        """
        excel = OperationExcel(excel_path=file_path)
        rows = excel.get_values()
        for i in range(len(rows)):
            if i >= start_index:
                line = f'{rows[i][1]}	{rows[i][2]}'
                os.environ["line"] = line
                # print(line)
                self.run("precision_data.intents_params")
                self.run("precision_data.faq_params")
        self.run("precision_data.agent_publish_params")

    def setup_class(self):
        """
        预知信息
        @return:
        """
        log.info("---setup class---")
        os.environ['pass_num'] = '0'
        os.environ['faild_num'] = '0'
        os.environ['sum_num'] = '0'

        # qury 前置
        # os.environ["agent_id"] = '5885'  # 中文保时捷
        # os.environ['agent_id'] = '5851'  # 中文伊利
        # os.environ['agent_id'] = '5944'  # 中文中华
        # os.environ['agent_id'] = '6003'  # dior
        # os.environ['agent_id'] = '6013'  # Nike
        # #
        # if os.path.exists("result/ceall_rate.txt") == True:
        #     os.remove('result/ceall_rate.txt')
        #
        self.run("channels_sort_class.channels_setup_class_1")
        headers = get_headers()
        log.info(f"headers:{headers}")
        self.run("channels_sort_class.channels_setup_class_auth_1")

    @pytest.mark.skip()
    def test_001(self):
        """
        创建dior机器人faq
        """
        file_path = '/Users/chengxinfei/Documents/GitHub/BlackManba/data/QAtestdata/Dior.traindata'
        self.run("precision_data.app_params")
        self.create_skills(file_path)

    @pytest.mark.skip()
    def test_002(self):
        """
        创建nike机器人faq
        """
        file_path = '/Users/chengxinfei/Documents/GitHub/BlackManba/data/QAtestdata/Nike.traindata'
        self.run("precision_data.app_params_1")
        self.create_skills(file_path)

    @pytest.fixture(params=query_skills())
    def create_data(self, request):
        return request.param

    @pytest.mark.skip()
    def test_003(self, create_data):
        """
        对dior/nike进行query
        """

        os.environ["query"] = create_data
        self.run("precision_data.query_pre_params")
        recall_rate(create_data)

    @pytest.mark.skip()
    def test_004(self):
        """
        创建英文测试机器人3
        """
        file_path = '/Users/chengxinfei/Documents/GitHub/BlackManba/data/QAtestdata/{quora英文测试（勿动）}知识点_2021-03-23 03_24_45(1).xlsx'
        self.run("precision_data.app_params_2")
        self.create_excel_agent(file_path, 0)

    @pytest.mark.skip()
    def test_005(self):
        """
        创建中华测试机器人3
        """
        file_path = '/Users/chengxinfei/Documents/GitHub/BlackManba/data/QAtestdata/中华IT.xlsx'
        self.run("precision_data.app_params_3")
        self.create_excel_agent(0, file_path)

    @pytest.fixture(params=query_excel(0))
    def create_data_2(self, request):
        return request.param

    @pytest.mark.skip()
    def test_006(self, create_data_2):
        """
        excel进行query
        """
        os.environ["query"] = create_data_2
        self.run("precision_data.query_pre_params")
        recall_rate(create_data_2)

    @pytest.mark.skip()
    def test_007(self):
        """
        创建保时捷测试机器人
        """
        file_path = '/Users/chengxinfei/Documents/GitHub/BlackManba/data/QAtestdata/保时捷set.xlsx'
        self.run("precision_data.app_params_4")
        self.create_excel_agent(0, file_path)

    # @pytest.mark.skip()
    def test_008(self):
        """
        创建伊利测试机器人
        """
        file_path = '/Users/chengxinfei/Documents/GitHub/BlackManba/data/QAtestdata/伊利set.xlsx'
        # self.run("precision_data.app_params_5")
        os.environ["agent_id"]="102449"
        for i in range(15):
            self.create_excel_agent(0, file_path)

    def teardown_class(self):
        print('=========teardown=========')
        print(int(os.environ["pass_num"]), int(os.environ["sum_num"]))
        with open('result/ceall_rate.txt', 'a+') as file:
            file.write(f'recall rate:{round(int(os.environ["pass_num"]) / int(os.environ["sum_num"]), 2) * 100}%')


def recall_rate(create_data):
    """
    计算召回率
    """
    log.debug(create_data)
    log.debug(os.environ.get('res_environ'))
    res_dict = json.loads(os.environ.get('res_environ'))
    res_answer = str(res_dict["data"]["responses"][0]["msg_body"]["text"]["content"]).strip()
    data_list = str(create_data).split('	')
    check_answer = str(data_list[1]).replace('/', ' or ').strip()
    if res_answer != check_answer:
        os.environ['faild_num'] = str(int(os.environ['faild_num']) + 1)
        with open('result/ceall_rate.txt', 'a+') as file:
            file.write(f'query:{data_list[0]}\tcheck:{check_answer}\tres:{res_answer}\n')
    else:
        os.environ['pass_num'] = str(int(os.environ['pass_num']) + 1)
    os.environ['sum_num'] = str(int(os.environ['sum_num']) + 1)
