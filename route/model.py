#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @Time    : 2020/3/2 16:26
#  @Author  : Evan.hu
#  @File    : model

import json,traceback
from TestCases.runserver import ExecutorTestCase
from entity import opertation_file
from entity.opertation_file import getServer, file_clear
from route import route_blue
from TestCases.entrance import restart
from TestCases import entrance
from flask import request, jsonify
from route.common.StartServerHandle import isRunPara, initEnv
from concurrent.futures import ThreadPoolExecutor

thread_pool = ThreadPoolExecutor(20)


@route_blue.route('/run/<server>/<model>', methods=['GET'])
def start(server,model):
    # 获取测试用例模块
    date = isRunPara(server,model)
    if isinstance(date,int):
        if date == 0:
            return jsonify(msg="测试用例微服务参数错误,没有找到该微服务测试用例:{server}".format(server=server), status="fail")
        elif date == 1:
            return jsonify(msg="测试用例执模块参数,没有找到该模块测试用例:{model}".format(model = model), status="fail")
        else:
            return jsonify(msg="测试用例微服务和模块不对应", status="fail")

    serverName = date[0]
    modelName = date[1]
    try:
        # 检查服务是否启动,如果服务启动则停止服务
        entrance.stop()

        # 运行测试用例
        entrance.run(server=serverName, model=modelName)
        # 启动报告服务
        entrance.restart()
    except Exception as e:
        msg = traceback.format_exc()
        return jsonify(msg="测试用例执行过程异常: {msg}".format(msg=msg), status="fail")
    return jsonify(msg="测试用例执行完毕", status="succ")

@route_blue.route('/v1/run/<server>/<model>', methods=['GET'])
def start_v1(server,model):
    # 获取测试用例模块
    date = isRunPara(server,model)
    if isinstance(date,int):
        if date == 0:
            return jsonify(msg="测试用例微服务参数错误,没有找到该微服务测试用例:{server}".format(server=server), status="fail")
        elif date == 1:
            return jsonify(msg="测试用例执模块参数,没有找到该模块测试用例:{model}".format(model = model), status="fail")
        else:
            return jsonify(msg="测试用例微服务和模块不对应", status="fail")

    serverName = date[0]
    modelName = date[1]
    try:
        # 检查服务是否启动,如果服务启动则停止服务
        entrance.stop()
        file_clear()

        # 运行测试用例
        thread_pool.submit(ExecutorTestCase, server=serverName, model=modelName)

    except Exception as e:
        msg = traceback.format_exc()
        return jsonify(msg="测试用例执行过程异常: {msg}".format(msg=msg), status="fail")
    return jsonify(msg="测试用例执行完毕", status="succ")

@route_blue.route('/switch/env', methods=['POST'])
def switch_environment():
    if request.method == 'POST':
        try:
            data = dict(json.loads(request.get_data(as_text=True)))
            keys = data.keys()
        except Exception as e:
            return jsonify(msg="json数据格式错误", status="200")
        if 'new_ip' in keys:
            new_ip = data['new_ip']
        else:
            new_ip = ''

        if 'new_port' in keys:
            new_port = data['new_port']
        else:
            new_port = ''

        env = opertation_file.alter_env(new_ip, new_port)
        return jsonify(msg="succ", current=env, status="200")

@route_blue.route('/reload')
def reload():
    restart()
    return jsonify(msg="服务重启", status="200")

@route_blue.route('/init')
def init():
    # 初始化系统服务
    date = initEnv()
    msg = str(date).encode()
    if date == 0:
        return jsonify(msg="系统初始化成功", status="succ")

    return jsonify(msg=msg , status="fail")

@route_blue.route('/get/case')
def getTestCase():
    TestCase = getServer(True)
    return jsonify(msg=TestCase, status="succ")

@route_blue.route('/hello/<server>/<model>',methods=['GET'])
def hello(server,model):
    return "12"
