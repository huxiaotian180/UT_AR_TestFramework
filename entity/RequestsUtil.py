#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 15:10
# @Author  : Evan.hu
import requests, json,traceback


# 重构
class Request:
    # 2、定义公共方法
    # def __init__(self):
    #     self.log = TestLog().getlog()

    def requests_api(self, url, headers, date, info, method):
        info['log'].info('接口{method}请求开始:{server}-->{model}-->{testCase}'.format(method=method,server=info['TestCaseServer'],model=info['TestCaseModel'],testCase=info['TestCaseName']))
        if method == "get":
            # get请求
            try:
                r = requests.get(url, data=json.dumps(date), headers=headers)
            except Exception as e:
                # traceback.print_exc()
                info['log'].info(traceback.format_exc())
                info['flag'] = False
                info['skipMeg'] = '接口请求错误: {msg}'.format(msg=traceback.format_exc())
        elif method == "post":
            # post请求
            try:
                r = requests.post(url, data=json.dumps(date), headers=headers)
            except Exception as e:
                traceback.print_exc()
                info['log'].info(traceback.format_exc())
                info['flag'] = False
                info['skipMeg'] = '接口请求错误: {msg}'.format(msg=traceback.format_exc())
        elif method == "delete":
            # delete请求
            try:
                r = requests.delete(url, data=json.dumps(date), headers=headers)
            except Exception as e:
                traceback.print_exc()
                info['log'].info(traceback.format_exc())
                info['flag'] = False
                info['skipMeg'] = '接口请求错误: {msg}'.format(msg=traceback.format_exc())
        elif method == "put":
            # put请求
            try:
                r = requests.put(url, data=json.dumps(date), headers=headers)
            except Exception as e:
                traceback.print_exc()
                info['log'].info(traceback.format_exc())
                info['flag'] = False
                info['skipMeg'] = '接口请求错误: {msg}'.format(msg=traceback.format_exc())

        # 获取结果内容
        try:
            body = r.json()
        except Exception as e:
            body = r.text

        # 内容存到字典
        info['url'] = url
        info['headers'] = headers
        info['payload'] = json.dumps(date)
        info['code'] = r.status_code
        info['response'] = body

    # 3、重构get/post方法
    def get(self, url, headers, date, info, method='get', **kwargs):
        # 2、定义参数
        # 3、调用公共方法
        return self.requests_api(url, headers, date, info, method, **kwargs)

    def post(self, url, headers, date, info, method='post', **kwargs):
        # 2、定义参数
        # 3、调用公共方法
        return self.requests_api(url, headers, date, info, method, **kwargs)

    def delete(self, url, headers, date, info, method='delete', **kwargs):
        # 2、定义参数
        # 3、调用公共方法
        return self.requests_api(url, headers, date, info, method, **kwargs)

    def put(self, url, headers, date, info, method='put', **kwargs):
        # 2、定义参数
        # 3、调用公共方法
        return self.requests_api(url, headers, date, info, method, **kwargs)
