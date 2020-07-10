#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 9:57
# @Author  : Evan.hu
from API.backup import getFile
from CaseServices.AIScript.AIinterface import interfaceGen
from CaseServices.AIScript.AItestCse import caseGen
from CaseServices.AIScript.AItestData import caseDateGen
import json,os

def recoverDate():
    pass
def recoverAll():
    path = r'C:\UT_AR_TestFramework\API\backup'
    date = getFile(path)
    for server in date.keys():
        # 遍历所有测试用例
        for model in date[server]:
            for file in date[server][model]:
                namepath = path + os.path.sep + server + os.path.sep + model + os.path.sep + file + '.json'
                # 测试用例数据加载
                try:
                    CaseDate = json.load(open(namepath, 'r'))
                except Exception as e:
                    print(namepath)


                case = {
                 'server': CaseDate['Describe']['server'],
                 'model': CaseDate['Describe']['model'],
                 'TestCase': '',
                 'url': CaseDate['Describe']['url'],
                 'method': CaseDate['Describe']['method'],
                 'header': str(CaseDate['Describe']['header']),
                 'testcase_description': CaseDate['Describe']['interface_description'],
                 'Description' : '',
                 'body': '',
                 'interface_name': CaseDate['Describe']['interface_name'],
                 'verify': '',
                 'switch': CaseDate['Describe']['switch'],
                 'parameterize': '',
                 }

                CaseDate.pop('Describe')
                for Test in CaseDate.keys():

                    # 转化成Excel格式文件
                    case['TestCase'] = Test
                    case['Description'] = CaseDate[Test]['test_description']
                    case['body'] = str(CaseDate[Test]['body'])
                    case['verify'] = str(CaseDate[Test]['verify'])
                    case['parameterize'] = CaseDate[Test]['preposition']['parameterize']
                    case['OperationDb'] = CaseDate[Test]['preposition']['isOperationDb']
                    case['runflag'] = CaseDate[Test]['runflag']


                    # 生成测试接口
                    interfaceGen(case)

                    # 写入测试用例
                    caseGen(case)

                    # 生成测试用例数据
                    caseDateGen(case)
#
# if __name__ == '__main__':
#     path = r'C:\UT_AR_TestFramework\API\backup'
#     date = reload()
#     print(date)
#     reload()