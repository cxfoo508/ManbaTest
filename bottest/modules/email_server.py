import os
import yagmail
from yagmail.error import YagInvalidEmailAddress, YagConnectionClosed, YagAddressError

from bottest.modules.helper import file_path
from bottest.modules.logger import log


class Email:
    @staticmethod
    def send_email(recipients=None):
        try:
            filename = file_path() + "/report/TestReport.html"
            if os.path.exists(filename):
                contents = "发送内容可见附件"
                subject = "接口自动化测试报告"
                mail_to = recipients or eval(os.environ.get("mail_to"))
                yag = yagmail.SMTP(user="pdnotify@laiye.com", password="bGFpeWUxMjM0Cg==", host="smtp.exmail.qq.com")
                yag.send(
                    to=mail_to,
                    subject=subject,
                    contents=contents,
                    attachments=filename,
                )
                log.debug("recipients: %s" % mail_to)
                log.debug("subject: %s" % subject)
                log.debug("contents: %s" % contents)
                log.debug("attachments: %s" % filename)
            else:
                print("未生存自动化测试报告")
        except SyntaxError as e:
            print("邮箱信息有误", e)
        except YagInvalidEmailAddress as e:
            log.error("InvalidEmailAddress")
            log.exception(e)
        except YagAddressError as e:
            log.error("AddressError")
            log.exception(e)
        except YagConnectionClosed as e:
            log.error("ConnectionClosedError")
            log.exception(e)
