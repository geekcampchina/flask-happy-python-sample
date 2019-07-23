#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.common import application
from lib.common import config
from flask import jsonify
import services


@application.route("/", methods=['GET'])
def get_root():
    return jsonify({'result': 'Hello World!'})


@application.route("/getUserInfo", methods=['GET'])
def get_today_work_overview():
    return jsonify(services.get_user_info())

if __name__ == "__main__":
    application.run(
        host=config.listen,
        port=config.port,
        debug=config.debug
    )
