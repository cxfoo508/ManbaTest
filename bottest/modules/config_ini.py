"""
Create by 吹着风的包子 on 2018/11/20
"""
__author__ = "吹着风的包子"

import configparser
import codecs
from bottest.modules.helper import file_path
from loguru import logger

from bottest.modules.logger import log


class Config:
    path = file_path()
    manhattan_conf = path + "/data/api_data.ini"
    conf_par = configparser.ConfigParser()

    def __init__(self, file_need=manhattan_conf, error_key=""):
        if file_need == "":
            self.config_file = self.manhattan_conf
        else:
            self.config_file = file_need
        self.error_key = error_key
        self.conf_par.read(self.config_file, encoding="utf-8-sig")
        self.group = "API"

    def get(self, item):
        """
        获取ini文件
        :param item:
        :return:
        """
        try:
            info = self.conf_par.get(self.group, item)
            log.debug("正确读取信息: Key: %s Value: %s " % (item, str(info)))
        except configparser.NoSectionError:
            self.conf_par.add_section(self.group)
            self.conf_par.set(self.group, item, "")
            with codecs.open(self.config_file, "w", "utf-8-sig") as f:
                self.conf_par.write(f)
            info = self.conf_par.get(self.group, item)
            log.debug("正确读取信息: Key: %s Value: %s " % (item, str(info)))
        except configparser.NoOptionError:
            self.conf_par.set(self.group, item, "")
            with codecs.open(self.config_file, "w", "utf-8-sig") as f:
                self.conf_par.write(f)
        except Exception as e:
            info = self.error_key
            log.error(e, self.group, item, info)
        return info

    def set(self, item, value):
        """
        写入ini文件
        :param item:
        :param value:
        :return:
        """
        if self.group not in self.conf_par.sections():
            self.conf_par.add_section(self.group)
        str_value = str(value)
        self.conf_par.set(self.group, item, str_value)
        # Running the tests highlights that we do not close file object explicitly in many places of the code.
        # In Python 3.4+ this raises warnings such as:
        with codecs.open(self.config_file, "w", "utf-8-sig") as f:
            self.conf_par.write(f)
        log.debug("完成存储Key: %s ---Value: %s " % (item, str_value))


conf = Config()
