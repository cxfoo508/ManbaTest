"""
Create by 吹着风的包子 on 2019-07-11
"""
__author__ = "吹着风的包子"

import json
import random
import time
import requests

from loguru import logger as log

from requests_toolbelt import MultipartEncoder
from tenacity import retry, stop_after_attempt, wait_random, TryAgain

webhook_key = "2ec4dc46-ab50-42da-83b5-d5509e8ec149"
# webhook_key = "28d31427-c953-47ee-b7d0-6d774283167a"


class WeChatServer:
    @staticmethod
    @retry(wait=wait_random(min=1, max=2), stop=stop_after_attempt(4))
    def send_info(content):
        data = {"msgtype": "markdown", "markdown": content}
        response = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=%s" % webhook_key,
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        r_json = response.json()
        if r_json["errcode"] == -1:
            raise TryAgain
        log.info("发送消息:%s" % response.json())

    @staticmethod
    @retry(wait=wait_random(min=1, max=2), stop=stop_after_attempt(4))
    def upload_file(filepath, filename):
        with open(filepath + filename, "rb") as f:
            file_payload = {"filename": (filename, f, "application/octet-stream")}
            header_data = MultipartEncoder(
                file_payload,
                boundary="-----------------------------"
                + str(random.randint(1e28, 1e29 - 1)),
            )

            post_file_url = (
                "https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=%s&type=file"
                % webhook_key
            )
            response = requests.post(
                url=post_file_url,
                data=header_data,
                headers={"Content-Type": header_data.content_type},
            )
            r_json = response.json()
        log.info("上传文件:%s" % response.json())
        if r_json["errcode"] == -1:
            raise TryAgain
        elif r_json["media_id"]:
            return r_json["media_id"]

    @staticmethod
    @retry(wait=wait_random(min=1, max=2), stop=stop_after_attempt(4))
    def send_file(media_id):
        time.sleep(3)
        data = {"msgtype": "file", "file": {"media_id": media_id}}
        response = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=%s" % webhook_key,
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        r_json = response.json()
        if r_json["errcode"] == -1:
            raise TryAgain
        log.info("发送文件:%s" % response.json())



