import os
import zlib

import requests

from bottest.modules.logger import log


class Faye_tool:

    @staticmethod
    def faye_upload_all(file_path, file_name):
        """
        上传文件到云文档
        """
        url = 'http://47.95.98.104:10000/faye/file/upload'
        payload = {
            "name": file_name
        }
        files = [
            ('file', ('chatbot_report.html', open(file_path, 'rb'),
                      'text/html'))
        ]
        headers = {
        }
        print(payload,url)
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        log.info(f"UPLOAD RES:{response.text}")
        print(response.json())
        down_url = 'https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/all/'
        return down_url + (response.json())['data']['file_token']

    @staticmethod
    def faye_send(inter_body):
        """
        飞书-发送消息
        """
        header = {
            "Content-Type": "application/json"
        }
        faye_url = "http://47.95.98.104:10000/faye/msg/send"
        res = requests.post(url=faye_url, json=inter_body, headers=header)
        print(res)
