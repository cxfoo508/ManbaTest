"""
Create by 吹着风的包子 on 2018/11/20
"""
import os

__author__ = "吹着风的包子"

from loguru import logger as log


def api_path():
    """
    测试用例路径地址
    :return:
    """
    case_path = os.environ.get("case_path")
    if case_path:
        log.info("Get case path success: %r " % case_path)
        return case_path
    else:
        log.error("Get case path error!!!")
        raise ValueError


def test_case():
    """
    测试用例名称填写test_*.py可扫描所有文件
    :return:
    """
    case_file = os.environ.get("test_case")
    if case_file:
        log.info("Search case file ------: %r" % case_file)
        return case_file
    else:
        log.error("Search case error!!!")
        raise ValueError


def process_num():
    """
    测试用例名称填写test_*.py可扫描所有文件
    :return:
    """
    num = os.environ.get("process_num")
    if num:
        log.info("Search process_num ------: %r" % num)
        return num
    else:
        log.error("process_num error!!!")
        raise ValueError


def project_name():
    """
    测试用例名称填写test_*.py可扫描所有文件
    :return:
    """
    name = os.environ.get("project")
    if name:
        log.info("Search project ------: %r" % name)
        return name
    else:
        log.error("project error!!!")
        raise ValueError


def report_path():
    """
    测试报告地址
    """
    name = os.environ.get("report_path")
    if name:
        log.info("Search report path ------: %r" % name)
        return name
    else:
        log.error("report path error!!!")
        raise ValueError


def report_send():
    """
    报告发送
    :return:
    """
    name = os.environ.get("send_report")
    if name:
        log.info("Search send_report ------: %r" % name)
        return name
    else:
        log.error("project error!!!")
        raise ValueError


def get_api_url(url_type=None):
    """
    根据测试名称读取Url
    :return:
    """
    if url_type:
        web_url = os.environ.get(url_type + "_url")
        log.info("Get url type is: %r" % url_type)
    else:
        web_url = os.environ.get("url")
    if web_url:
        log.info("Get url success: %r" % web_url)
        return web_url
    else:
        log.error("Get url error")
        raise ValueError


def get_app_id():
    """
    :return:
    """

    app_id = os.environ.get("app_id")
    if app_id:
        log.info("Get app_id success: %r" % app_id)
        return int(app_id)
    # else:
    #     log.error("获取app_id错误")
    #     raise ValueError


def get_pubkey():
    """
    :return:
    """

    pubkey = os.environ.get("pubkey")
    if pubkey:
        log.info("Get pubkey success: %r" % pubkey)
        return pubkey
    # else:
    #     log.error("获取pubkey错误")
    #     raise ValueError


def get_secret():
    """
    :return:
    """

    secret = os.environ.get("secret")
    if secret:
        log.info("Get secret success: %r" % secret)
        return secret
    # else:
    #     log.error("获取secret错误")
    #     raise ValueError
