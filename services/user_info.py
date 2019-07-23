#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import inspect

from flask import request
from happy_utils import ParameterManager
from lib.util import make_api_response

from lib.common import hlog

ARG_FLAG_COMPANY_ID = 1 << 0
ARG_FLAG_USER_ID = 2 << 0


def check_company_id(company_id):
    """
    验证公司编号
    :param company_id:
    :return: bool
    """

    return company_id and len(company_id) >= 3

def check_user_id(user_id):
    """
    验证用户编号
    :param user_id:
    :return: bool
    """

    return user_id and len(user_id) >= 3

pm = ParameterManager()
pm.register_para(ARG_FLAG_COMPANY_ID, 'company_id', check_company_id)
pm.register_para(ARG_FLAG_USER_ID, 'user_id', check_user_id)


def get_user_info():
    func_name = inspect.stack()[0][3]
    hlog.enter_func(func_name)

    pm.enable_paras(ARG_FLAG_COMPANY_ID|ARG_FLAG_USER_ID)
    result = pm.validate_paras(request.args)

    if not result[0]:
        hlog.exit_func(func_name)
        return make_api_response(1, result[1])

    company_id = request.args.get('company_id')
    user_id = request.args.get('user_id')
    hlog.var('company_id', company_id)
    hlog.var('user_id', user_id)

    today_date = datetime.date.today()
    hlog.var('today_date', today_date)

    result = {
        "code": 0,
        "message": "",
        "obj": {
            "companyId": company_id,
            "date": str(today_date),
            "userId": user_id
        }
    }

    hlog.var('result', result)

    hlog.exit_func(func_name)
    return result