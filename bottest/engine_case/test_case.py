# coding = utf-8
import json

import pytest

from engine_case.engine_base_case import *

dialog_data_1 = ["0_/restart", "1_奶粉结块", "2_刚开封", "3_包装完好"]  # 对话树
dialog_data_2 = ["0_/restart", "1_奶粉结块调查", "2_刚开封", "3_打开前好像有点漏气"]
dialog_data_3 = ["0_/restart", "1_奶粉结块调查", "2_使用一段时间后", "3_在保质期"]
dialog_data_4 = ["0_/restart", "1_奶粉结块调查", "2_使用一段时间后", "3_过保质期了"]
dialog_data_5 = ["0_/restart", "1_奶粉结块调查", "2_dfgdfgdfg", "3_sdfsdfsdfsdf", "4_sdafasdfadf"]
form_data = ["0_/restart", "1_官网申请试用", "2_小明", "3_COVID-19会引发哪些症状", "4_来也科技", "5_我来自北京", "6_334433@qq.com",
             "7_可以"]  # form
form_data_1 = ["0_/restart", "1_官网申请试用", "2_小王", "3_来也科技", "4_2012-11-11", "5_帝都", "7_334433@qq.com", "10_可以"]  # form
form_data_2 = ["0_/restart", "1_官网申请试用", "2_小王", "3_来也科技", "4_2012-11-11", "5_中国", "6_北京", "7_北京", "8_海淀区",
               "9_13911154620", "10_132201198905082931", "11_334433@qq.com", "12_可以"]
form_data_3 = ["0_/restart", "1_官网申请试用", "2_小fff王", "3_来也科技", "4_2012-11-11", "5_中国", "6_北京", "7_北京", "8_海淀区",
               "9_13911154620", "10_132201198905082931", "11_334433@qq.com", "12_可以"]
form_data_4 = ["0_/restart", "1_官网申请试ddd用", "2_小王", "3_来也科技", "4_2012-11-11", "5_中国", "6_北京", "7_北京", "8_海淀区",
               "9_13911154620", "10_132201198905082931", "11_334433@qq.com", "12_可以"]
# wulai_data = ["1_restart"]

# def get_data():
# return

userid=str(uuid.uuid4()).replace('-','')
@pytest.fixture(params=dialog_data_1)
def send_data(request):
    return request.param


def test_001_query(send_data):
    """
       对话树-query
       """
    # print(send_data)
    data = send_data.split("_")
    print(data[1])
    res = query(data[1],userid=userid)
    print(res.status_code, res.content.decode())
    res_con = json.loads(res.content.decode())


data = ['新冠风险人群.find({患病群体: "老年人"})', '新冠风险人群.find({患病群体: {$eq: "老年人"}})', '新冠风险人群.find({患病群体: 老年人}, {})',
        '新冠风险人群.findOne({患病群体: "老年人"})', '新冠风险人群.find({患病群体: {$contains: "老"}})',
        '新冠风险人群.find({患病群体: "老年人"}, {是否属于高风险: 1})', '新冠风险人群.find({患病群体: "老年人"}, {最低年龄: 0, 最高年龄: 0})',
        '新冠风险人群.find({最高年龄: {$gte: 20, $lte: 60}})', '新冠风险人群.find({是否属于高风险: "属于"}, {患病群体: 1})',
        '新冠风险人群.find({患病群体: "儿童", 最高年龄: {$gte: 10, $lte: 60}})',
        '新冠风险人群.find({最高年龄: {$eq: 200}})',
        '新冠风险人群.find({最高年龄: {$gt: 60}})',
        '新冠风险人群.find({最高年龄: {$lt: 200}})',
        '新冠风险人群.find({最高年龄: {$gte: 0}})',
        '新冠风险人群.find({最高年龄: {$lte: 60}})',
        '新冠风险人群.find({$and: [{患病群体: "儿童"}, {最高年龄: {$gte: 20, $lte: 200}}]})',
        '新冠风险人群.find({$or: [{患病群体: "儿童"}, {最高年龄: {$gte: 20, $lte: 60}}]})',
        '新冠风险人群.findOne({$or: [{患病群体: "儿童"}, {最高年龄: {$gte: 20, $lte: 60}}]})']

data_update = ['新冠风险人群.update({患病群体: {$eq: "老年人"}}, {患病群体: "老人"})', '新冠风险人群.find({患病群体: "老人"})',
               '新冠风险人群.update({患病群体: {$eq: "老点多年人"}}, {患病群体: "老d人"}, {upsert: true})', '新冠风险人群.find({患病群体: "老d人"})',
               '新冠风险人群.update({患病群体: {$eq: "老多年人"}}, {患病群体: "老f人"}, {upsert: false})', '新冠风险人群.find({患病群体: "老f人"})',
               '新冠风险人群.update({最低年龄: {$eq: "20"}}, {最低年龄: "10"}, {upsert: false})', '新冠风险人群.find({最低年龄: "10"})',
               '新冠风险人群.updateOne({最低年龄: {$eq: "10"}}, {最低年龄: "20"}, {upsert: false})', '新冠风险人群.find({最低年龄: "20"})']
data_insert = ['新冠风险人群.insert({患病群体: "青少年", 是否属于高风险: "属于", 最高年龄: 20, 最低年龄: 10})', '新冠风险人群.find({患病群体: "青少年"})',
               '新冠风险人群.update({患病群体: {$eq: "青少年"}}, {患病群体: "青少年g"})', '新冠风险人群.find({患病群体: "青少年g"})',
               '新冠风险人群.insert([{患病群体: "青少年1", 是否属于高风险: "属于", 最高年龄: 20, 最低年龄: 10},{患病群体: "中年人", 是否属于高风险: "属于", 最高年龄: 30, 最低年龄: 60}])',
               '新冠风险人群.find({$or: [{患病群体: "青少年1"}, {患病群体: "中年人"}]})']


@pytest.fixture(params=data_insert)
def send_data_2(request):
    return request.param


def test_002_table_read(send_data_2):
    """
    table read
    """
    data = send_data_2
    res = query_table(data)
    con = res.content.decode()
    print(con)
