#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
API 操作相关
"""

import inspect

from happy_utils import HappyLog
from happy_utils import HappyPyException

_hlog = HappyLog.get_instance('')


def make_api_response(code: int, message: str, data=None, token_str=None):
    """
    构造接口响应内容

    :rtype:
    :param code: 响应代码
    :param message: 消息
    :param data:  返回内容
    :param token_str:  token
    :return: dict
    """

    func_name = inspect.stack()[0][3]
    _hlog.enter_func(func_name)

    _hlog.var('code', code)
    _hlog.var('message', message)
    _hlog.var('data', data)
    _hlog.var('token_str', token_str)

    if data is None:
        data = {}

    if not isinstance(data, dict):
        raise HappyPyException('参数 data 类型必须为 dict')

    res = {
        'code': code,
        'message': message if message else '',
        'obj': data if data else '{}'
    }

    if token_str:
        res['tokenStr'] = token_str

    _hlog.var('res', res)

    _hlog.exit_func(func_name)
    return res
