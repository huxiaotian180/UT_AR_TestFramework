#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @Time    : 2020/3/2 16:25
#  @Author  : Evan.hu
#  @File    : __init__.py

from flask import Blueprint  # 先导入蓝图函数

route_blue = Blueprint('route', __name__)

from route import model
