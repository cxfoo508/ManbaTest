# coding = utf-8

from copy import deepcopy

import pandas
import yaml
from pandas import DataFrame

agent_id = []


class OperationExcel(object):
    def __init__(self, excel_path=None):
        if excel_path != None:
            engine = "openpyxl"
            self.file = pandas.read_excel(excel_path, engine=engine)
            self.values = self.file.values

        self.file_path = excel_path

    def add_excle(self, name, head_data, index):
        """
        创建excle
        head_data:{"index": [], "intent": [], 'skills': []}
        """
        # 构建数据
        df = pandas.DataFrame(head_data)
        # 设置ID为索引（默认再添加一列新的数据）
        df = df.set_index(index)
        # 写入数据（to_excel方法（此处写至001.xlsx中））
        df.to_excel(name)
        return df

    def get_len(self):
        """
        row len
        """
        return len(self.file.values)

    def add_row(self, df, index, data, file_path):
        """
        增加一行数据
        index:第一列
        data:['data'，'data']
        """
        df.loc[index] = data
        df.to_excel(file_path)

    def get_values(self):
        """
        read excel
        """
        return self.values

    def get_one_value(self, index):
        """
        读取一行
        """
        data = self.file.values[index]
        return data

    def update_excel(self, row_index, col_index, up_data, sheet_name="Sheet1", index=False, header=True):
        """
        修改excel
        """
        self.values[row_index][col_index] = up_data
        DataFrame(self.values).to_excel(self.file_path, sheet_name=sheet_name, index=index, header=header)


class OperationYaml(object):
    def __init__(self, yaml_path):
        self.file = open(yaml_path, "r", encoding='utf-8')
        self.cfg = self.file.read()

    def load_yaml(self):
        return yaml.load(self.cfg)

    def dict_yaml(self, excel_path):
        file = OperationExcel(excel_path)
        intents = list()
        intent = dict()
        utter_faq = dict()
        for i in file.values:
            if "/" in i[1]:
                i[1] = i[1].replace("/", "")
                intent["intent"] = "faq|" + i[1]
            else:
                intent["intent"] = "faq|" + i[1]
            utter_faq_key = "utter_faq|" + i[1]
            utter_faq[utter_faq_key] = i[4]
            if "||" in i[2]:
                examples_value = i[2].split("||")
            else:
                examples_value = []
                examples_value.append(i[2])
            intent["examples"] = examples_value
            if str(i[4]) == "nan":
                utter_faq[utter_faq_key] = {"response_mode": 'all',
                                            "response": []}
            else:
                if isinstance(i[4], str):
                    value = i[4].strip().replace("_x000d_", "")
                    utter_faq[utter_faq_key] = {"response_mode": 'all',
                                                "response": [{"text": value}]}
                else:
                    value = i[4]
                    utter_faq[utter_faq_key] = {"response_mode": 'all',
                                                "response": [{"text": value}]}
            intents.append(deepcopy(intent))  # 解决list append过程中值被覆盖问题
        return intents, utter_faq

    def dict_yaml_one(self, excel_path, new_yaml_path):
        file = OperationExcel(excel_path)
        intents = list()
        intent = dict()
        utter_faq = dict()
        for i in file.values:
            if "/" in i[1]:
                i[1] = i[1].replace("/", "")
                intent["intent"] = "faq|" + i[1]
            else:
                intent["intent"] = "faq|" + i[1]
            utter_faq_key = "utter_faq|" + i[1]
            utter_faq[utter_faq_key] = i[4]
            if "||" in i[2]:
                examples_value = i[2].split("||")
            else:
                examples_value = []
                examples_value.append(i[2])
            intent["examples"] = examples_value
            if str(i[4]) == "nan":
                utter_faq[utter_faq_key] = {"response_mode": 'all',
                                            "response": []}
            else:
                if isinstance(i[4], str):
                    value = i[4].strip().replace("_x000d_", "")
                    utter_faq[utter_faq_key] = {"response_mode": 'all',
                                                "response": [{"text": value}]}
                else:
                    value = i[4]
                    utter_faq[utter_faq_key] = {"response_mode": 'all',
                                                "response": [{"text": value}]}
            intents.append(deepcopy(intent))  # 解决list append过程中值被覆盖问题
        dict_yaml_value = self.load_yaml()
        dict_yaml_value["intents"] = intents
        dict_yaml_value["faqs"] = utter_faq
        file = open(new_yaml_path, "w", encoding="utf-8")
        yaml.dump(dict_yaml_value, file, allow_unicode=True, default_flow_style=False,
                  sort_keys=False)  # 该行的代码中sort_keys的默认值为True，改为Flase后可修复代顺序变化的问题
        file.close()


def main():
    excel_path = ["../data/{51Talk（未缩减）}知识点_2021-03-31 07_08_25.xlsx",
                  "../data/{Dior知识库（未缩减）}知识点_2021-03-31 07_03_51.xlsx",
                  "../data/{Nike知识库（未缩减）}知识点_2021-03-31 07_05_06.xlsx",
                  "../data/{新东方（未缩减）}知识点_2021-03-31 07_07_51.xlsx",
                  "../data/{育学园（未缩减）}知识点_2021-03-31 07_02_33.xlsx"]
    yaml_path = "../domain.yaml"
    new_yaml_path = "../domain_z.yaml"
    intents_list = []
    utter_faq_dict = {}
    for i in excel_path:
        intents, utter_faq = OperationYaml(yaml_path).dict_yaml(i)
        intents_list.extend(deepcopy(intents))
        utter_faq_dict.update(utter_faq)
    dict_yaml_value = OperationYaml(yaml_path).load_yaml()
    print(dict_yaml_value["faqs"])
    dict_yaml_value["intents"] = intents_list
    dict_yaml_value["faqs"] = utter_faq_dict
    file = open(new_yaml_path, "w", encoding="utf-8")
    yaml.dump(dict_yaml_value, file, allow_unicode=True, default_flow_style=False,
              sort_keys=False)  # 该行的代码中sort_keys的默认值为True，改为Flase后可修复代顺序变化的问题
    file.close()

# if __name__ == '__main__':
# excel_path = "../data/{新东方（未缩减）}知识点_2021-03-31 07_07_51.xlsx"
# yaml_path = "../domain.yaml"
# new_yaml_path = "../domain4.yaml"
# OperationYaml(yaml_path).dict_yaml_one(excel_path, new_yaml_path)
# excel = OperationExcel('../data/副本1.xlsx')
# head = {"index":[],"intent":[]}
# path = '../data/测试.xlsx'
# df=excel.add_excle(path,head,"index")
# print(excel.get_len())
# excel.add_row(df,1,["哈哈哈"],path)
# excel.add_row(df,1,['dddd'],path)
