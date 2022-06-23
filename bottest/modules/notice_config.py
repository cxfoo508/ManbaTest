# 发送邮件参数配置
import os

EMAIL_NAME = "Laiye"
EMAIL_HOST = "smtp.exmail.qq.com"
EMAIL_USER = "pdnotify@laiye.com"
EMAIL_PWD = "bGFpeWUxMjM0Cg=="

RUN_MAX = 6
# 运行成功邮件参数配置
SUCCESS_SUBJECT = "接口自动化测试报告--成功报告"
FAIL_SUBJECT = "接口自动化测试报告--失败报告"
recipients = eval(os.environ.get("mail_to"))

# 发送通知到钉钉
