import datetime
import json
import os
from pathlib import Path

from bottest.modules.faye_server import Faye_tool
from bottest.modules.html_control import html_control


class SendMsg(html_control):
    @staticmethod
    def get_inter_body(**kwargs):
        """
        根据执行情况获取不同body
        """
        inter_body = {
            "msg_type": "interactive",
            "card": {
                "config": {
                    "wide_screen_mode": True
                },
                "header": {
                    "title": {
                        "tag": "plain_text",
                        "content": "🚴‍♀️🚴‍♂️🚴ChartBotReport📑"
                    },
                    "template": "green"
                },
                "elements": [
                    {
                        "tag": "div",
                        "text": {
                            "tag": "lark_md",
                            "content": ''
                        }
                    },
                    {
                        "tag": "action",
                        "actions": [
                            {
                                "tag": "button",
                                "text": {
                                    "tag": "plain_text",
                                    "content": "下载报告"
                                },
                                "type": "primary",
                                "url": ''
                            },

                        ]
                    }
                ]
            }

        }

        # 用例连续成功
        if kwargs['type'] == 1:
            inter_body['card']['elements'][0]['text'][
                'content'] = f"测试地址：{kwargs['url']}\n用例成功执行: {kwargs['success_num']} \n用例失败执行: {kwargs['fail_num']}"
            inter_body['card']['elements'][1]['actions'][0]['url'] = kwargs['down_url']
        # 用例失败
        elif kwargs['type'] == 2:
            inter_body['card']['elements'][0]['text'][
                'content'] = f"测试地址：{kwargs['url']}\n用例成功执行: {kwargs['success_num']} \n用例失败执行: {kwargs['fail_num']}\n成功率: {kwargs['statistics_info']}"
            inter_body['card']['elements'][1]['actions'][0]['url'] = kwargs['down_url']
            inter_body['card']['header']['template'] = 'red'
        # 用例回复正常
        elif kwargs['type'] == 3:
            inter_body['card']['elements'][0]['text'][
                'content'] = f"测试地址：{kwargs['url']}\n用例总数: {kwargs['success_num']} \n成功率: 100%"
            del (inter_body['card']['elements'][1])
            inter_body['card']['header']['template'] = 'yellow'
        elif kwargs['type'] == 4:
            inter_body['card']['header']['title'][
                'content'] = f"🚴‍♀️🚴‍♂️🚴老板错误数量超过{kwargs['fail_num']}个了😈👿👿"
            inter_body['card']['header']['template'] = 'red'
            del (inter_body['card']['elements'][0])
            del (inter_body['card']['elements'][0])

        return inter_body

    @classmethod
    def send_msg(cls):
        is_send = os.environ.get("send_report")
        if is_send == 'True':
            # 飞书
            path = str(Path(__file__).parent.parent) + '/report/'
            time_s = (str((datetime.datetime.now())).replace(' ', "&"))[:-7]
            report_name = f'chatbot_report_{time_s}.html'
            down_url = Faye_tool.faye_upload_all((path + "test.html"), report_name)
            url = os.environ.get('url')

            pass_num, faild_num, sum_num = cls.get_report_data(path)
            statistics = round(pass_num / sum_num, 2) * 100

            type_report = 1 if faild_num == 0 else 2
            inter_body = cls.get_inter_body(type=type_report, url=url, success_num=pass_num, fail_num=faild_num,
                                            statistics_info=f'{statistics}%',
                                            down_url=down_url)
            Faye_tool.faye_send(inter_body)

    @classmethod
    def send_msg_v1(cls, path):
        is_send = os.environ.get("send_report")
        project = os.environ.get("project")
        if is_send == 'True':
            # 飞书
            time_s = (str((datetime.datetime.now())).replace(' ', "&"))[:-7]
            report_name = f'chatbot_report_{time_s}.html'
            down_url = Faye_tool.faye_upload_all(f"{path}/{project}.html", report_name)
            url = os.environ.get('url')
            pass_num, faild_num, sum_num = cls.get_report_data(path)
            statistics = round(pass_num / sum_num, 2) * 100
            color_value = "green"
            case_status = "通过"
            if int(faild_num) > 0:
                color_value = "red"
                case_status = "不通过"
            test_name = 'Chatbot'
            test_user_id = 152850099
            test_user_name = '关璐'
            test_content = "{\"config\": {\"wide_screen_mode\": true}, \"header\": {\"title\": {\"tag\": \"plain_text\", " \
                           "\"content\": \"📣📣📣 👉%s👈测试报告📰\"}, \"template\": \"%s\"}, \"elements\": [{\"tag\": \"div\", " \
                           "\"text\": {\"tag\": \"lark_md\", \"content\": \"💬测试环境地址：%s \\n❤用例执行总数: %d \\n💚用例成功执行: %d \\n💔用例失败执行: %d\\n👁️‍成功率: %d %% \\n🗨测试结果: %s \"}}, " \
                           "{\"tag\": \"action\", \"actions\": [{\"tag\": \"button\", \"text\": {\"tag\": \"plain_text\", \"content\": \"👉下载报告\"}, " \
                           "\"type\": \"primary\", \"url\": \"%s\"}]}, {\"tag\": \"div\", \"fields\": [{\"is_short\": false, \"text\": " \
                           "{\"tag\": \"lark_md\", \"content\": \"<at id=%d>%s</at>\"}}]}]}" \
                           % (test_name, color_value, url, int(sum_num), int(pass_num), int(faild_num), int(statistics),
                              case_status, down_url, int(test_user_id),
                              test_user_name)
            inter_body = {
                "receive_id": "oc_6c10a943c218d98586cffe5b3f783185",
                "msg_type": "interactive",
                "content": test_content
            }
            Faye_tool.faye_send(inter_body)

    @classmethod
    def send_json(cls, json_save_path):
        """
        测试结果以json方式保存到文件
        """
        json_data = {"code": 0, "msg": "succeed", "data": "congratulation"}
        json_name = "results.json"
        if not os.path.exists(json_save_path):
            os.makedirs(json_save_path, exist_ok=True)
        pass_num, faild_num, sum_num = cls.get_report_data(json_save_path)
        if faild_num != 0:
            json_data["code"] = 1000
            json_data["msg"] = "failed"
            json_data["data"] = "please check the report"
        with open(f'{json_save_path}/{json_name}', 'w') as file:
            file.write(json.dumps(json_data))


if __name__ == "__main__":
    pass
