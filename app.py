#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @Time    : 2020/3/2 16:30
#  @Author  : Evan.hu
#  @File    : app.py

from flask import Flask
from route import route_blue

__author__ = 'Evan.hu'

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(route_blue)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
