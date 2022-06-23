# coding =utf-8
import datetime
import os
import random
import uuid

import shortuuid

from bottest.modules.helper import file_path as fp
from bottest.modules.licence_control import MinnioOper


def Unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)


def get_str(num):
    strs = [Unicode() for i in range(num)]
    return ''.join(strs)


def get_string(num):
    """
    根据uuid获取随机字符串
    """
    return shortuuid.ShortUUID().random(length=num)


def get_numbers(num):
    """
    生成数字随机串
    """
    su = shortuuid.ShortUUID(alphabet="0123456789")
    nid = int(su.random(length=num))
    return nid


def exist_object(key, data):
    if key in data.keys():
        return True
    else:
        return False


def get_int(num):
    new_num = ""
    for i in range(int(num)):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        new_num += ch
    return int(new_num)


def get_param_list(param_list, class_name, parm_name=None) -> list:
    """
    返回变量名称集合
    """
    lists = []
    if parm_name is None:
        for i in param_list:
            if "case" in i:
                lists.append(class_name + i)
    elif type(parm_name) == list:
        for i in param_list:
            if "case" in i:
                lists.append(class_name + i)
        lists = lists[parm_name[0]: parm_name[1]]
    else:
        for item in param_list:
            if parm_name == item:
                lists.append(class_name + item)
    return lists


def get_param_list_v2(param_list, cls_obj, parm_name=None) -> list:
    """
    返回变量名称集合
    """
    lists = []
    if parm_name is None:
        for i in param_list:
            if "case" in i:
                lists.append(eval(f'cls_obj.{i}'))
    elif type(parm_name) == list:
        for i in param_list:
            if "case" in i:
                lists.append(eval(f'cls_obj.{i}'))
        lists = lists[parm_name[0]: parm_name[1]]
    else:
        for item in param_list:
            if parm_name == item:
                lists.append(eval(f'cls_obj.{item}'))
    return lists


def get_uuid():
    """
    uuid
    """
    uid = uuid.uuid4()
    return str(uid).replace('-', '')


def get_time_now(time_formate):
    """
    获取当前时间并且格式化
    @param time_formate: "%Y-%m-%dT%H:%M:%SZ"
    @return:
    """
    UTC_FORMAT = time_formate
    time_now = datetime.datetime.now()
    time = time_now.strftime(UTC_FORMAT)
    return time


def update_dict(param):
    """
    替换json中的函数参数
    """
    param_type = type(param)
    type_list = ["get_str", 'get_int', 'os.environ', 'get_uuid', 'get_time_now','get_numbers','get_string','get_upload_minio_url']
    if param_type == dict:
        for key in param.keys():
            if type(param[key]) in [dict, list]:
                update_dict(param[key])
            else:
                for i in type_list:
                    if i in str(param[key]):
                        b = os.environ.get('0')  # 此行没用
                        param[key] = eval(param[key])
    elif param_type == list:
        for i in range(len(param)):
            if type(param[i]) in [dict, list]:
                update_dict(param[i])
            else:
                for v in type_list:
                    if v in str(param[i]):
                        b = os.environ.get('0')
                        param[i] = eval(param[i])


def get_upload_minio_url(file_name, file_suffix):
    """
    获取上传minio后的url,文件的保存在data目录中
    @param file_name: 上传文件名称 如xxx.img
    @param file_suffix: 文件的后缀名 比如 img
    @return: 上传minio后返回的url
    """
    file_path = os.path.join(fp(), f"data/{file_name}")
    minio_url = os.environ.get("minio_url")
    if minio_url and (minio_url != ""):
        minio_access_key = os.environ.get("minio_access_key")
        minio_secret_key = os.environ.get("minio_secret_key")
        bucket_name = "chatbot"
        minio_client = MinnioOper(minio_url, access_key=minio_access_key, secret_key=minio_secret_key)
        # 上传
        bucket_list = minio_client.get_bucket_list()
        print(bucket_list)
        minio_client.upload_file(bucket_name, file_name, file_path, file_suffix)
        up_url = minio_client.presigned_get_file(bucket_name, file_name)
        return up_url
