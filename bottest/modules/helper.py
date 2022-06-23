"""
Create by 吹着风的包子 on 2018/11/20
"""
import argparse
import logging
import os
import socket

from dotenv import load_dotenv, find_dotenv

__author__ = "吹着风的包子"


def file_path():
    """
    路径拼写
    :return:
    """
    root_path = os.path.dirname(os.path.abspath(__file__))
    project_path = root_path[: root_path.rfind("bottest") + len("bottest")]
    return project_path


def _choose_environ():
    parser = argparse.ArgumentParser(description="This is a PyMOTW sample program")
    parser.add_argument(
        "-env", type=str, dest="environment", help="the running environment", default=""
    )
    args = parser.parse_args()
    environ = args.environment
    return environ


# def _choose_environ():
#     parser = argparse.ArgumentParser(description="This is a PyMOTW sample program")
#     parser.add_argument("-t", "--test", dest="TEST", help="the running environment", action="store_true")
#     args = parser.parse_args()
#     return args.TEST


def set_allure_url():
    """
    设置报告地址
    """
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    path = f'{file_path()}/allure-results/environment.properties'
    file_data = ''
    with open(path, 'r') as f:
        for line in f.readlines():
            if 'baseUrl' in line:
                line = f'baseUlr=http://{ip}'
            file_data += line
    with open(path, 'w') as f:
        f.write(file_data)


def init():
    if not _choose_environ():
        environ = os.environ.get("ENV")
    else:
        environ = _choose_environ()  # 获取命令行传过来的环境变量
    filename = "config.test" if (not environ or environ == "default") else f"config.{environ}"

    envfiles = find_dotenv(filename="%s/configs/%s" % (os.getcwd(), filename))
    load_dotenv(envfiles, verbose=True)
    print("ENV is `%s`" % os.environ.get("ENV"))
    print("Looking for env file %s \n" % filename)
    root_dir = os.path.dirname(os.path.abspath(__file__))

    os.environ.setdefault("ROOT_DIR", root_dir)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("faker").setLevel(logging.WARNING)
