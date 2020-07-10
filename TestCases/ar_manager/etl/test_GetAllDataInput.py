#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @Time    : 2020/6/4 16:22
#  @Author  : Evan.hu

from entity import operation_logging, TestCaseDateManger
from interface.ar_manager.etl.GetAllDataInput import GetAllDataInput_get
from entity.Allure import Allure
import pytest, allure, os

# 初始化日志
log = operation_logging.TestLog().getlog()
path = os.path.split(os.path.abspath(__file__))
case_info = TestCaseDateManger.TestCasePre(path)
pytestmark = TestCaseDateManger.isSkip(case_info)

@allure.feature(case_info['server'])
@allure.issue("http://confluence.eisoo.com/pages/viewpage.action?pageId=69144480", name='点击我跳转需求文档')
@allure.testcase("http://jira.eisoo.com", name='点击我跳转到缺陷管理')
class Test_etl(object):
    @allure.story(case_info['model'])
    @pytest.mark.parametrize('key', case_info['key'])
    def test_GetAllDataInput_get(self, key):
        parameter = case_info['date'][key]
        info = TestCaseDateManger.dataManger(case_info, parameter, GetAllDataInput_get, log)

        # 接口断言
        Allure(info).step()
        Allure(info).Assert()

if __name__ == '__main__':
    pytest.main()