#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import PurePath

from flask import Flask
from flask_cors import CORS
from happy_utils import HappyConfigParser
from happy_utils import HappyLog

from lib.config import Config
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    """ 支持正则的路由判断
    Example::
        Rule('/<regex(r"\d+"):lang_code>')
    :param map: the :class:`Map`.
    """
    def __init__(self, map, *args):
        BaseConverter.__init__(self, map)
        self.regex = args[0]


CONFIG_DIR = PurePath(__file__).parent.parent / 'configs'
CONFIG_FILENAME = str(CONFIG_DIR / 'common.ini')
LOG_CONFIG_FILENAME = str(CONFIG_DIR / 'log.ini')

config = Config()
HappyConfigParser.load(CONFIG_FILENAME, config)

# 为支持 uWSGI 默认加载点，Flask 应用名称不能修改
application = Flask('api-python-sample')
# 支持 JSON 显示中文
application.config['JSON_AS_ASCII'] = False
# 前端夸域
CORS(application)
application.url_map.converters['regex'] = RegexConverter

hlog = HappyLog.get_instance(LOG_CONFIG_FILENAME)
