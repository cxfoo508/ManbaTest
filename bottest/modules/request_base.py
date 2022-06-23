import hashlib
import json
import os
import random
import string
import time

import requests

from bottest.modules.logger import log

CHAR_LIST = []

[[CHAR_LIST.append(e) for e in string.digits] for i in range(0, 2)]
[[CHAR_LIST.append(e) for e in string.digits] for i in range(0, 2)]
[[CHAR_LIST.append(e) for e in string.digits] for i in range(0, 2)]


def GetChars(length):
    random.shuffle(CHAR_LIST)
    return "".join(CHAR_LIST[0:length])


def rear_post(url, data, url_ver=1, url_encode=0):
    """
    后端请求
    """
    send_url = url
    URL = os.environ.get('url')
    token = os.environ.get("token")
    header = auth_headers()
    log.info(f"send header:{header}")
    url_s = f"{URL}{send_url}"
    res = requests.post(url=url_s, json=data, headers=header, timeout=10)
    log.info(f'send url: {res.url}')
    log.info(f'res time: {res.elapsed.total_seconds()}')
    return res


def rear_get(url, data=None, url_ver=1):
    """
    后端請求
    """
    send_url = url
    URL = os.environ.get('url')
    token = os.environ.get("token")
    # header = {
    #     "Content-Type": "application/json",
    #     "Authorization": f"Bearer {token}"
    # }
    header = auth_headers()
    log.info(f"send header:{header}")
    # log.info(f'send url: {URL}{send_url}')
    res = requests.get(url=f"{URL}{send_url}", params=data, headers=header, timeout=10)
    log.info(f'send url:{res.url}')
    log.info(f'res time: {res.elapsed.total_seconds()}')
    return res


def rear_del(url, data=None, url_ver=1):
    """
    后端請求
    """
    send_url = url
    URL = os.environ.get('url')
    token = os.environ.get("token")
    # header = {
    #     "Content-Type": "application/json",
    #     "Authorization": f"Bearer {token}"
    # }
    header = auth_headers()
    log.info(f"send header:{header}")
    log.info(f'send url: {URL}{send_url}')
    res = requests.delete(url=f"{URL}{send_url}", json=data, headers=header)
    log.info(f'res time: {res.elapsed.total_seconds()}')
    return res


def get_headers():
    """
    获取渠道header
    """
    # 开放平台的基础信息
    # secret = "W8AF78C8A9AEEDF774062AC7E600513E"
    # pubkey = "M937AB21C263110E"
    secret = os.environ.get("account_secret")
    pubkey = os.environ.get("account_key")
    log.info(f"pubkey:{pubkey}")
    log.info(f"secret:{secret}")
    # 秒级别时间戳
    timestamp = str(int(time.time()))
    nonce = GetChars(32)
    sign = hashlib.sha1((nonce + timestamp + secret).encode()).hexdigest()
    data = {
        "account_key": pubkey,
        "nonce": nonce,
        "sign": sign,
        "timestamp": timestamp
    }
    os.environ["auth_account_key"] = pubkey
    os.environ["auth_nonce"] = nonce
    os.environ["auth_sign"] = sign
    os.environ["auth_timestamp"] = timestamp
    headers = {}
    for k, v in data.items():
        headers["auth_" + k] = v
    return headers


def channel_auth(data=None):
    """
    获取渠道权鉴Token
    """
    log.info(f'data:{data}')
    url = '/v1/channels/auth'
    res = rear_post(url, data)
    con = res.content.decode()
    log.info(f'res:{con}')
    return con


def get_channel_auth():
    headers = get_headers()
    res = channel_auth(data=headers)
    con_data = json.loads(res)
    return con_data["data"]["access_token"]


def request_data_channel(url, data=None):
    """
    渠道post
    """
    send_url = url
    URL = os.environ.get("url")
    token = os.environ.get("access_token")
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    log.info(f"Bearer {token}")
    log.info(f"{URL}{send_url}")
    request_channel = requests.post(url=f"{URL}{send_url}", json=data, headers=header)
    log.info(f'res time: {request_channel.elapsed.total_seconds()}')
    return request_channel


def auth_headers():
    """
    获取header
    """
    secret = os.environ.get("account_secret")
    pubkey = os.environ.get("account_key")
    log.info(f"pubkey:{pubkey}")
    log.info(f"secret:{secret}")
    # 秒级别时间戳
    timestamp = str(int(time.time()))
    nonce = GetChars(32)
    sign = hashlib.sha1((nonce + timestamp + secret).encode()).hexdigest()
    headers = {
        "Content-Type": "application/json",
        "Api-Auth-pubkey": pubkey,
        "Api-Auth-nonce": nonce,
        "Api-Auth-sign": sign,
        "Api-Auth-timestamp": timestamp
    }
    return headers
