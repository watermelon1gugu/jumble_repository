# encoding = utf-8
"""

@author archchen
@time 2019-07-28 14:33
"""
import json
import logging

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.DEBUG)


class _Logger:
    def __init__(self, name):
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(logging.DEBUG)

    def debug(self, info):
        """
        :param info: 打印的日志信息
        :desc  只打印日志信息
        """
        self.__logger.debug("[DEBUG]" + info)

    def debug(self, info, req):
        """
        :param info: 日志信息主体
        :param req: 请求object
        :desc: 会按照info中的格式进行格式化输出 例如 "test info req:{}"
        """
        self.__logger.debug("[DEBUG]" + info.format(json.dumps(req.__dict__)))

    def debug(self, info, req, res):
        """
        :param info: 日志信息主体
        :param req: 请求object
        :param res: 请求处理结果object
        :desc 会按照info中的格式进行格式化输出 例如 "test info req:{} res:{}"
        """
        self.__logger.debug("[DEBUG]" + info.format(json.dumps(req.__dict__), json.dumps(res.__dict__)))

    def info(self, info):
        """
        :param info: 打印的日志信息
        :desc  只打印日志信息
        """
        self.__logger.debug("[info]" + info)

    def info(self, info, req):
        """
        :param info: 日志信息主体
        :param req: 请求object
        :desc: 会按照info中的格式进行格式化输出 例如 "test info req:{}"
        """
        self.__logger.debug("[info]" + info.format(json.dumps(req.__dict__)))

    def info(self, info, req, res):
        """
        :param info: 日志信息主体
        :param req: 请求object
        :param res: 请求处理结果object
        :desc 会按照info中的格式进行格式化输出 例如 "test info req:{} res:{}"
        """
        self.__logger.debug("[info]" + info.format(json.dumps(req.__dict__), json.dumps(res.__dict__)))


class Loggers:
    """
    :desc 对外暴露的Logger配置类
    """
    API_LOGGER = _Logger("API_LOGGER")
    TEST_LOGGER = _Logger("TEST_LOGGER")
