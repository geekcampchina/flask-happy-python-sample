#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from happy_utils import HappyConfigBase


class Config(HappyConfigBase):
    """
    配置文件模板
    """
    def __init__(self):
        super().__init__()

        self.section = 'api-python-sample'
        self.listen = ''
        self.port = 0
        self.debug = True