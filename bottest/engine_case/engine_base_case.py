import uuid

import requests

URL = "http://172.17.202.22:5015"
URL_tab = "http://172.17.202.22:5020"


def request_data(url, data=None, check_data=None, type="post"):
    """
    request
    """
    send_url = url
    header = {
        "Content-Type": "application/json"
    }

    if type == "post":
        print(f"{URL}{send_url}")
        request = requests.post(url=f"{URL}{send_url}", json=data, headers=header)
    else:
        print(data)
        request = requests.get(url=f'{URL_tab}{send_url}', params=data)
        request.encoding = 'utf-8'
        print(request.url)
    return request


def query_table(data):
    """
    table
    """
    userid = ''.join(str(uuid.uuid4()).split('-'))
    print(f"user_id: {userid}")
    body = {

        "agent_id": 0,
        "table_query": data
    }
    url = "/table/execute"
    res = request_data(url, data=body, check_data=None, type='get')
    return res


def query(data, userid=True):
    """

    """
    if userid == True:
        userid = ''.join(str(uuid.uuid4()).split('-'))
    print(f"user_id: {userid}")
    body = {
        "msg_body": {
            "text": {
                "content": data
            }
        },
        "metadata": [],
        "agent_id": 0,
        "user_id": userid,
        "skill_ids": [
            0
        ],
        "debug": False
    }
    url = "/core/engine/dm/bot-response"
    res = request_data(url, data=body)
    return res
