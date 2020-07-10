#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 17:32
# @Author  : Evan.hu
from entity.operation_yaml import operation_yaml_read,search_file
from assertContent.AssertRoute.AssertRouteRule import AssertRule
from entity.JsonPath import parse_json,seekKey
import os,copy,traceback

class Framework(object):
    def __init__(self,flag,server,model,name):
        self.info = {}
        self.flag = flag
        self.server = server
        self.model = model
        self.name = name
        self.__PATH = r'C:\UT_AR_TestFramework\requestBody'
        self.__FILENAME = 'RequestBody' + '.yaml'
        self.__FILEPATH = self.__PATH + os.path.sep + self.server + os.path.sep + self.model + os.path.sep + self.name

    def readfile(self,server,model,name):
        filePath = self.__PATH + os.path.sep + server + os.path.sep + model + os.path.sep + name
        fileName = 'RequestBody' + '.yaml'
        # 查看是否存在测试用例
        flag = search_file(filePath + os.path.sep + fileName)
        return flag

    def readCase(self,dateReq):
        for key in self.info['date'].keys():
            body = self.info['date'][key]['req_body']
            # 实例化请求body
            if len(body) > 0:
                paraId = list(body.keys())
                # 获取接口请求body
                json_data = copy.deepcopy(dateReq['body'])

                # 測試用例設計参数化替换
                for id in paraId:
                    try:
                        # 读取测试用例参数化数据
                        context = body[id]
                        self.info['reqPareBody'][id] = body[id]

                        # 测试数据设计类型替换
                        data_struct_list = []
                        data_struct_link = 'json_data'
                        parse_json(json_data, data_struct_link, data_struct_list)
                        ReqBody = seekKey(json_data, data_struct_list, id, context)
                        self.info['date'][key]['req_body'] = ReqBody

                    except Exception as e:
                        self.info['flag'] = False
                        self.info['skipMeg'] = '测试用例参数化替换程序异常：{msg}'.format(msg = traceback.format_exc())
            else:
                # 如果没有参数化数据，查看是否存在body
                if dateReq.get('body') is not None:
                    self.info['date'][key]['req_body'] = copy.deepcopy(dateReq['body'])
                else:
                    self.info['date'][key]['req_body'] = ''

            # 实例化断言,获取断言类型
            try:
                AssertId, AssertKey, AssertValue, AssertDb,AssertFlag = '', '', '', '',''
                type = self.info['date'][key]['verify']['AssertType']

                if self.info['date'][key]['verify'].get('id') is not None:
                    AssertId = self.info['date'][key]['verify']['id']

                if self.info['date'][key]['verify'].get('key') is not None:
                    AssertKey = self.info['date'][key]['verify']['key']

                if self.info['date'][key]['verify'].get('value') is not None:
                    AssertValue = self.info['date'][key]['verify']['value']

                if self.info['date'][key]['verify'].get('db') is not None:
                    AssertDb = self.info['date'][key]['verify']['db']

                if self.info['date'][key]['verify'].get('flag') is not None:
                    AssertFlag = self.info['date'][key]['verify']['flag']

                AssertDate = AssertRule(type=type, id=AssertId, key=AssertKey, value=AssertValue, db=AssertDb,flag=AssertFlag)
                self.info['date'][key]['verify'] = AssertDate

            except Exception as e:
                self.info['flag'] = False
                self.info['skipMeg'] = '测试用例断言格式错误: {msg}'.format(msg=traceback.format_exc())

    def skip(self):
        if self.flag:
            self.info['reqPareBody'] = {}
            self.info['urlParameter'] = ''
            self.info['server'] = ''
            self.info['method'] = ''
            self.info['date'] = []
            self.info['key'] = []
            self.info['model'] = ''
            self.info['story_description'] = '{name}测试用例skip'.format(name=self.name)
            self.info['Requests'] = ''
            self.info['switch'] = False

        else:
            CASE_INFO = operation_yaml_read(self.server,self.model, self.name)
            if CASE_INFO is None:
                self.info['reqPareBody'] = {}
                self.info['urlParameter'] = ''
                self.info['server'] = ''
                self.info['method'] = ''
                self.info['date'] = []
                self.info['key'] = []
                self.info['model'] = ''
                self.info['story_description'] = '{name}测试用例skip'.format(name=self.name)
                self.info['Requests'] = ''
                self.info['switch'] = False
                self.info['readExcept'] = True
                return self.info

            self.info['reqPareBody'] = {}
            self.info['urlParameter'] = CASE_INFO['request']['url_path']
            self.info['server'] = CASE_INFO['server']
            self.info['method'] = CASE_INFO['request']['method']
            self.info['date'] = copy.deepcopy(CASE_INFO['testcases'])
            # 读取测试用例
            self.readCase(CASE_INFO)
            self.info['key'] = list(CASE_INFO['testcases'].keys())
            self.info['model'] = CASE_INFO['model']
            self.info['story_description'] = CASE_INFO['story_description']
            self.info['Requests'] = CASE_INFO['request']
            self.info['switch'] = CASE_INFO['switch']
            if CASE_INFO.get('transaction') is not None:
                self.info['transaction'] = CASE_INFO['transaction']

        return self.info


# if __name__ == '__main__':
#     date = Framework(True,'','').skip()
#     print(date['date'])
