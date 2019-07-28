import json
import logging

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.DEBUG)


class _Logger:
    def __init__(self, name):
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(logging.DEBUG)

    def debug(self, info):
        self.__logger.debug("[DEBUG]" + info)

    def debug(self, info, req):
        self.__logger.debug("[DEBUG]" + info.format(json.dumps(req.__dict__)))

    def debug(self, info, req, res):
        self.__logger.debug("[DEBUG]" + info.format(json.dumps(req.__dict__), json.dumps(res.__dict__)))


class Loggers:
    API_LOGGER = _Logger("API_LOGGER")
