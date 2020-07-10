#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 15:02
# @Author  : Evan.hu
from assertContent.assertInferfaceCode import assertCode
from assertContent.assertInterfaceDelete import assertDelete
from assertContent.assertInterfaceGet import assertGetCount, assertGetAll, assertGetId
from assertContent.assertInterfaceKey import assertKey
from assertContent.assertInterfacePut_2 import assertPut
from assertContent.assertInterfacePost import assertPost
from assertContent.assertPrefix import assertPrefix
import allure,pytest

class Allure(object):
    def __init__(self,info):
        self.info = info

    def step(self):
        if self.info['flag'] :
            with allure.step("测试用例描述"):
                context = self.info['original_date']['Description']
                allure.attach('description', '测试用例描述 : {description}'.format(description=context))

            with allure.step("请求URL"):
                allure.attach('URL', 'url : {value}'.format(value=self.info['url']))

            with allure.step("请求headers"):
                if self.info.get('headers') is not None:
                    headers = self.info['headers']
                    for key in headers.keys():
                        allure.attach('headers', '{key} : {value}'.format(key=key, value=headers[key]))

            with allure.step("请求参数"):
                body = self.info['request_data']
                if len(body) != 0:
                    allure.attach('请求参数', 'Body : {body}'.format(body=body))

            with allure.step("接口Response"):
                if self.info.get('response') is not None:
                    if len(self.info['response']) != 0:
                        allure.attach('接口返回body', 'Response body : {body}'.format(body=self.info['response']))

    def assertPre(self):
        self.info['log'].info('启用前置断言')
        msg = assertPrefix(self.info)
        if msg['actual']['flag']:
            allure.attach('实际结果',msg['actual']['msg'])
            assert False

    def assertCode(self):
        self.info['log'].info('启用断言：0机制')
        msg = assertCode(self.info)
        if msg['except']['code'] != msg['actual']['code']:
            allure.attach('期望结果',msg['except']['msg'])
            allure.attach('实际结果', msg['actual']['msg'])
            assert False


    def assertKeyValue(self):
        self.info['log'].info('启用断言：1机制')
        msg = assertKey(self.info)

        if msg.get('failed') is not None:
            allure.attach('返回报文异常',msg['failed'])
            assert False
        else:
            if msg['except']['keyValue'] != msg['actual']['keyValue']:
                allure.attach('期望结果',msg['except']['msg'])
                allure.attach('实际结果',msg['actual']['msg'])
                assert False


    def assertIsKeyExist(self):
        self.info['log'].info('启用断言：2机制')
        msg = assertPost(self.info)
        if msg.get('failed') is not None:
            allure.attach('返回报文异常',msg['failed'])
            assert False

        else:
            if msg['except']['flag'] != msg['actual']['flag']:
                allure.attach('期望结果',msg['except']['msg'])
                allure.attach('实际结果',msg['actual']['msg'])
                assert False


    def assertDelete(self):
        self.info['log'].info('启用断言：3机制')
        msg = assertDelete(self.info)
        if msg.get('isSkip') is not None:
            pytest.skip(msg['isSkip'])
        if not (msg['flag'] == True):
            allure.attach('期望结果',msg['msg']['expect'])
            allure.attach('实际结果',msg['msg']['actual'])
            allure.attach('查询sql',msg['msg']['sql'])
            allure.attach('sql查询结果',msg['msg']['sqlDate'])
            assert False

    def assertPut(self):
        self.info['log'].info('启用断言：4机制')
        msg = assertPut(self.info)
        if msg.get('isSkip') is not None:
            pytest.skip(msg['isSkip'])
        else:
            # 接口断言
            if msg['except']['flag'] != msg['actual']['flag']:
                allure.attach('期望结果', msg['except']['msg'])
                allure.attach('实际结果', msg['actual']['msg'])
                allure.attach('数据库信息', msg['db']['msg'])
                assert False

    def assertGetCount(self):
        self.info['log'].info('启用断言：5机制')
        msg = assertGetCount(self.info)

        if msg.get('isSkip') is not None:
            pytest.skip(msg['isSkip'])

        if not msg['flag']:
            allure.attach('期望结果',msg['msg']['except'])
            allure.attach('实际结果',msg['msg']['actual'])
            allure.attach('实际返回信息',msg['msg']['actualMsg'])
            assert False

    def assertGetId(self):
        self.info['log'].info('启用断言：6机制')
        msg = assertGetId(self.info)

        if msg.get('isSkip') is not None:
            pytest.skip(msg['isSkip'])

        if not msg['flag']:
            allure.attach('期望结果',msg['msg']['except'])
            allure.attach('实际结果',msg['msg']['actual'])
            assert False

    def assertGetAll(self):
        self.info['log'].info('启用断言：7机制')
        msg = assertGetAll(self.info)
        if not msg['flag']:
            allure.attach('get接口请求断言', msg['msg'])
            assert False

    def assertPass(self):
        self.info['log'].info('启用断言：PASS机制')
        allure.attach('test result', 'TEST PASS')

    def get_default(self):
        pass

    def Assert(self,**kwargs):
        switcher = {
            'prefix': self.assertPre,
            0: self.assertCode,    # 根据接口返回码判断
            1: self.assertKeyValue,  # 根据接口返回内容包含字段来判断,根据key和value来判断
            2: self.assertIsKeyExist,   # 根据接口返回字段是否包含key来判断,不需要关注key的具体值
            3: self.assertDelete, # 根据接口delete请求进行断言
            4: self.assertPut, # 根据接口put请求进行断言
            5: self.assertGetCount,
            6: self.assertGetId,
            7: self.assertGetAll,
            'default': self.assertPass
        }
        if self.info['flag']:
            with allure.step("缺陷描述"):
                AssertInfo = self.info['original_date']['verify']['AssertType']
                AssertInfo.insert(0,'prefix')
                AssertInfo.append('default')
                for key in AssertInfo:
                    switcher.get(key,self.get_default)()
        else:
            pytest.skip(msg="{msg}".format(msg=self.info['skipMeg']))