"""
Create by 吹着风的包子 on 2019-02-14
"""
import logging
import os
import sys

from loguru import logger

from bottest.modules.helper import file_path


LOG_DIR = os.path.join(os.getcwd(), "log")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)


def logger_init():
    logger.remove()  # Remove every possibly added handlers, including the default one

    fmt = "{time:YYYY-MM-DD HH:mm:ss:SSSS}|{level}:{message}"
    file_fmt = "/test-log-{time:YYYY-MM-DD}.log"
    logger.add(sys.stdout, format=fmt, level="DEBUG")
    logger.add(
        os.path.join(LOG_DIR) + file_fmt, format=fmt, level="DEBUG", retention="10 days", encoding='utf-8'
    )


logger_init()
log = logger
