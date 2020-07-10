#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @Time    : 2020/3/6 9:12
#  @Author  : Evan.hu
#  @File    : error


from flask import request, json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None,
                 headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url_no_param()
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]


class runException(Exception):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return self.info

def Test():
    try:
        name = input("enter your naem:")
        raise runException(name)
    except runException as e_result:
        msg = e_result
        return msg

if __name__ == '__main__':
    date = Test()
    print(type(date))