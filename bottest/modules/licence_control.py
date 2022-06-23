import os
import sys
import time
from datetime import timedelta

import requests
from minio import Minio
from minio.deleteobjects import DeleteObject
from minio.error import S3Error

from bottest.modules.helper import file_path as fp
from bottest.modules.request_base import auth_headers

URL = os.environ.get("url")
licence_name = "chatbot-agents-poc.lcs"
licence_path = os.path.join(fp(), f"data/licences/{licence_name}")


def get_licence_list():
    """
    获取licence
    @return: licence list
    """
    url = f"{URL}/chatbot/v1alpha1/licenses"
    header = auth_headers()
    res = requests.get(url, headers=header, timeout=5)
    return res.json()


def licence_uplaod(li_url):
    """
    上传licence
    @return:
    """
    url = f"{URL}/chatbot/v1alpha1/license"
    dict_data = {
        "uri": li_url
    }
    # header = {
    #     "Content-Type": "application/json"
    # }
    header = auth_headers()
    res = requests.post(url, json=dict_data, headers=header)
    return res.json()


class MinnioOper:
    def __init__(self, service, access_key, secret_key, secure=False):
        if os.environ["minio_ssl"] == "True":
            secure = True
        self.service = service
        self.client = Minio(service, access_key=access_key, secret_key=secret_key, secure=secure)

    def exists_bucket(self, bucket_name):
        """
        判断桶是否存在
        :param bucket_name: 桶名称
        :return:
        """
        return self.client.bucket_exists(bucket_name=bucket_name)

    def create_bucket(self, bucket_name: str, is_policy: bool = False):
        """
        创建桶 + 赋予策略
        :param bucket_name: 桶名
        :param is_policy: 策略
        :return:
        """
        if self.exists_bucket(bucket_name=bucket_name):
            return False
        else:
            self.client.make_bucket(bucket_name=bucket_name)
        if is_policy:
            policy = self.policy % (bucket_name, bucket_name)
            self.client.set_bucket_policy(bucket_name=bucket_name, policy=policy)
        return True

    def get_bucket_list(self):
        """
        列出存储桶
        :return:
        """
        buckets = self.client.list_buckets()
        bucket_list = []
        for bucket in buckets:
            bucket_list.append(
                {"bucket_name": bucket.name, "create_time": bucket.creation_date}
            )
        return bucket_list

    def remove_bucket(self, bucket_name):
        """
        删除桶
        :param bucket_name:
        :return:
        """
        try:
            self.client.remove_bucket(bucket_name=bucket_name)
        except S3Error as e:
            print("[error]:", e)
            return False
        return True

    def bucket_list_files(self, bucket_name, prefix):
        """
        列出存储桶中所有对象
        :param bucket_name: 同名
        :param prefix: 前缀
        :return:
        """
        try:
            files_list = self.client.list_objects(bucket_name=bucket_name, prefix=prefix, recursive=True)
            for obj in files_list:
                print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
                      obj.etag, obj.size, obj.content_type)
        except S3Error as e:
            print("[error]:", e)

    def bucket_policy(self, bucket_name):
        """
        列出桶存储策略
        :param bucket_name:
        :return:
        """
        try:
            policy = self.client.get_bucket_policy(bucket_name)
        except S3Error as e:
            print("[error]:", e)
            return None
        return policy

    def download_file(self, bucket_name, file, file_path, stream=1024 * 32):
        """
        从bucket 下载文件 + 写入指定文件
        :return:
        """
        try:
            data = self.client.get_object(bucket_name, file)
            with open(file_path, "wb") as fp:
                for d in data.stream(stream):
                    fp.write(d)
        except S3Error as e:
            print("[error]:", e)

    def fget_file(self, bucket_name, file, file_path):
        """
        下载保存文件保存本地
        :param bucket_name:
        :param file:
        :param file_path:
        :return:
        """
        self.client.fget_object(bucket_name, file, file_path)

    def copy_file(self, bucket_name, file, file_path):
        """
        拷贝文件（最大支持5GB）
        :param bucket_name:
        :param file:
        :param file_path:
        :return:
        """
        self.client.copy_object(bucket_name, file, file_path)

    def upload_file(self, bucket_name, file, file_path, content_type):
        """
        上传文件 + 写入
        :param bucket_name: 桶名
        :param file: 文件名
        :param file_path: 本地文件路径
        :param content_type: 文件类型
        :return:
        """
        try:
            with open(file_path, "rb") as file_data:
                file_stat = os.stat(file_path)
                self.client.put_object(bucket_name, file, file_data, file_stat.st_size, content_type=content_type)
        except S3Error as e:
            print("[error]:", e)

    def fput_file(self, bucket_name, file, file_path):
        """
        上传文件
        :param bucket_name: 桶名
        :param file: 文件名
        :param file_path: 本地文件路径
        :return:
        """
        try:
            self.client.fput_object(bucket_name, file, file_path)
        except S3Error as e:
            print("[error]:", e)

    def stat_object(self, bucket_name, file):
        """
        获取文件元数据
        :param bucket_name:
        :param file:
        :return:
        """
        try:
            data = self.client.stat_object(bucket_name, file)
            print(data.bucket_name)
            print(data.object_name)
            print(data.last_modified)
            print(data.etag)
            print(data.size)
            print(data.metadata)
            print(data.content_type)
        except S3Error as e:
            print("[error]:", e)

    def remove_file(self, bucket_name, file):
        """
        移除单个文件
        :return:
        """
        self.client.remove_object(bucket_name, file)

    def remove_files(self, bucket_name, file_list):
        """
        删除多个文件
        :return:
        """
        delete_object_list = [DeleteObject(file) for file in file_list]
        for del_err in self.client.remove_objects(bucket_name, delete_object_list):
            print("del_err", del_err)

    def presigned_get_file(self, bucket_name, file, days=7):
        """
        生成一个http GET操作 签证URL
        :return:
        """
        return self.client.presigned_get_object(bucket_name, file, expires=timedelta(days=days))


def init_licence():
    """
    初始化licence
    @return:
    """
    minio_url = os.environ.get("minio_url")
    if minio_url and (minio_url != ""):
        minio_access_key = os.environ.get("minio_access_key")
        minio_secret_key = os.environ.get("minio_secret_key")
        bucket_name = "chatbot"
        minio_client = MinnioOper(minio_url, access_key=minio_access_key, secret_key=minio_secret_key)
        # 查询是否有licence
        licence_list = get_licence_list()
        if len(licence_list["licenses"]) == 0:
            # 上传
            minio_client.upload_file(bucket_name, licence_name, licence_path, "cls")
            licence_url = minio_client.presigned_get_file(bucket_name, licence_name)
            res = licence_uplaod(licence_url)
            if len(res["licenses"]) != 2:
                print("uplaod licence failed!!!")
                print(res)
                sys.exit()
        else:
            print("licence exist")
        time.sleep(2)
