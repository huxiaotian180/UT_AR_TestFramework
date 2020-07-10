#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 16:18
# @Author  : Evan.hu
from entity.operation_excel import OperationExcel
from CaseServices.AIScript.AIinterface import interfaceGen
from CaseServices.AIScript.AItestCse import caseGen
from CaseServices.AIScript.AItestData import caseDateGen

def AutoScript(name):
    # 读取接口测试数据
    opers = OperationExcel(name)
    line = opers.get_lines()
    for line in range(1, line):
        print(line)
        case = {}
        dict_key = opers.get_row_values(0)
        dic_value = opers.get_row_values(line)
        for date in zip(dict_key, dic_value):
            case[date[0]] = date[1]

        # 写入接口文件
        interfaceGen(case)

        # 写入测试用例
        caseGen(case)

        # 写入测试数据
        caseDateGen(case)

if __name__ == '__main__':
    name = "TestCase.xlsx"
    AutoScript(name)