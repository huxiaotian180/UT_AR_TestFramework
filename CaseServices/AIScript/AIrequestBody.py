#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 9:02
# @Author  : Evan.hu
from CaseServices.AIScript.comm.AItool import isdir
from entity.opertation_file import search_file
from entity.operationYaml import operationWrite
import os

BODY_PATH = r'C:\UT_AR_TestFramework\requestBody'


def bodyGen(info,date):
    server = info['server']
    model = info['model']
    name = 'Test' + '_' + info['interface_name']
    path = BODY_PATH + os.path.sep + server + os.path.sep + model + os.path.sep + name
    isdir(path)
    filename = 'RequestBody.yaml'
    filepath = path + os.path.sep + filename
    flag = search_file(filepath)
    if not flag:
        operationWrite(path,filename,date)

if __name__ == '__main__':
    info = {'server': 'ar_manager123', 'model': 'Role', 'TestCase': 'TestCase1', 'url': '/manager/user', 'method': 'post', 'header': '', 'testcase_description': '创建用户', 'Description': '正常场景:创建用户', 'body': '{\n    "roleName": "wsed",\n    "permissions": [\n        {\n            "permissionId": "ID_MAINPAGE",\n            "checked": false,\n            "name": "主页",\n            "isLeaf": 1,\n            "parentId": ""\n        },\n        {\n            "permissionId": "ID_SEARCH",\n            "checked": true,\n            "name": "搜索",\n            "isLeaf": 0,\n            "parentId": ""\n        }\n    ],\n    "resource": {\n        "logGroup": [\n            "fe5b7f96-443a-11e7-a467-000c29253e90",\n            "a0ead37a-89bf-11ea-a3db-0242ac120034"\n        ],\n        "jobTemplate": [\n            "686d78d2-7d39-11ea-99c3-0242ac120034"\n        ],\n        "dashboard": {\n            "dashboardId": [\n                "fbb1467e-129a-549b-58c2-1002e48d86af",\n                "f987638a-54d0-4ba5-5451-72a1ffb13637"\n            ],\n            "mainPageId": ""\n        }\n    },\n    "description": "12312312325",\n    "defaultLogGroupID": "fe5b7f96-443a-11e7-a467-000c29253e90"\n}', 'interface_name': 'UpdateManagerRole', 'parameterize': 'RoleID', 'verify': '{\n    "AssertType": [\n        0,\n        "default"\n    ],\n    "statusCode": {\n        "code": 200,\n        "expect_message": ""\n    }\n}'}
    date = {'a':2}
    bodyGen(info,date)
