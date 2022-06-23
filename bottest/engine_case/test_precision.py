# coding = utf-8
import json
from multiprocessing import Process

from engine_case.engine_base_case import *
from tools import build_module


# 准确率计算
# 1、读取数据表
# 2、进行query
# 3、记录相似问，回复意图，应该意图，正确数量，错误数，总数，计算召回率
class PrecisionCase:
    def __init__(self, address, name):
        self.path = address
        self.excel_name = name
        self.excel_path = self.path + self.excel_name + ".txt"
        self.sum_number = 0
        self.true_num = 0
        self.false_num = 0
        self.index = 0

    def run_query(self, df, data, save_path):
        """
        query 结果
        """
        row_data = []
        intent_name = data[2]
        query_data = str(data[1]).split('||')
        print(f'data len: {len(query_data)}')
        for i in query_data:
            print(f"send_data: {i}")
            res = query(i)
            print(f'res_code: {res.status_code},res_time:{res.elapsed.total_seconds()}')
            con = json.loads(res.content.decode())
            print(f"res:{res.content.decode()}")
            if 'faq' in str(con['intent']['name']):
                res_intent = (str(con["intent"]["name"]).split('|'))[1]
            else:
                res_intent = con['intent']['name']
            intent_name_s = (str(intent_name).replace('/', '')).split('||')
            if res_intent in intent_name_s:
                check = "True"
                print(f"result:True")
            else:
                check = "False"
                print("result:False")
            row_data.append(i)
            row_data.append(intent_name)
            row_data.append(res_intent)
            row_data.append(check)
            save_excel = build_module.OperationExcel()
            save_excel.add_row(df, self.index, row_data, save_path)
            self.index += 1
            row_data.clear()

    def process_index(self, index_s, rows_values, save_df, save_path):
        start_index = index_s[0]
        end_index = index_s[1]
        for i in range(len(rows_values)):
            print(start_index, end_index, i)
            if (i >= start_index) and (i <= end_index):
                self.run_query(save_df, rows_values[i], save_path)
            elif i > end_index and i != 0:
                break

    def open_text(self):
        """
        读取测试数据
        """
        file_path = self.excel_path
        sum_list = []
        with open(file_path, 'r') as file:
            while True:
                file_data = file.readline()
                if file_data != '':
                    row_l = file_data.replace('\n', '').split('\t')
                    sum_list.append(row_l)
                else:
                    break
        return sum_list

    def process_run(self, proce_num):
        """
        分配进程，一个文档按行数分配
        """
        # excel_data = build_module.OperationExcel(self.excel_path)
        # rows_values = excel_data.get_values()
        rows_values = self.open_text()
        # row_len = excel_data.get_len() - 1  # 第一行不是query数据
        row_len = len(rows_values)
        print(f"run row len:{row_len}")
        data_i = int(row_len / proce_num)
        data_y = int(row_len % proce_num)
        i_sum = []
        start = 1
        end = data_i
        for i in range(proce_num):
            li = []
            li.append(start)
            li.append(end)
            start += data_i
            if i == (proce_num - 2):
                end = end + data_i + data_y
            else:
                end += data_i
            i_sum.append(li)
        # print(i_sum)
        # run 进程
        proce_s = []
        save_excel_lis = []
        for i in range(proce_num):
            save_path = f'/Users/chengxinfei/Documents/GitHub/BlackManba/result/{self.excel_name}_process_{i}.xlsx'
            save_excel_lis.append(save_path)
            save_excel = build_module.OperationExcel()
            df = save_excel.add_excle(save_path,
                                      {"num": [], "query_data": [], "true_intent": [], "res_intent": [], "check": []}, 'num')
            pro = Process(target=self.process_index, args=(i_sum[i], rows_values, df, save_path))
            proce_s.append(pro)
        for p in proce_s:
            p.start()
        for p in proce_s:
            p.join()
        self.recall_rate(save_excel_lis)

    def recall_rate(self, files):
        """
        计算召回率
        """
        for f in files:
            df = build_module.OperationExcel(f)
            len = df.get_len()
            for i in range(len):
                row = df.get_one_value(i)
                answer = row[4]
                if answer:
                    self.true_num += 1
                else:
                    self.false_num += 1
                self.sum_number += 1
        recall = (str(round(self.true_num / self.sum_number, 2)).split("."))[1]
        print(f'sum_query:{self.sum_number},res_true:{self.true_num},res_false:{self.false_num}')
        print(f"recall:{recall}%")
        dff = build_module.OperationExcel()
        df_path = f"/Users/chengxinfei/Documents/GitHub/BlackManba/result/{self.excel_name}_recall.xlsx"
        df = dff.add_excle(df_path,
                           {"sum_query": [], "res_true": [], "res_false": [], 'recall': []},
                           "sum_query")
        dff.add_row(df, self.sum_number, [self.true_num, self.false_num, recall + "%"], df_path)


if __name__ == '__main__':
    # a = 'AC异常无法下载/安装'
    # print(a.replace('/',''))
    file_name = "test_cases"
    file_path = f"/Users/chengxinfei/Documents/GitHub/BlackManba/data/QA_English_Dataset/"
    pre = PrecisionCase(file_path, file_name)
    pre.process_run(10)
