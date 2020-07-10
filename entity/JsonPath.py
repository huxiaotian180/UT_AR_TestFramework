#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 17:17
# @Author  : Evan.hu

import re

def parse_json(json_data, data_struct_link,data_struct_list):
    '''
    递归解析json数据结构，存储元素的路径
    :param json_data:
    :param data_struct_link:
    :return:
    '''
    if type(json_data) == type({}):  # 字典类型
        keys_list = json_data.keys()
        for key in keys_list:
            temp_data_struct_link = data_struct_link + '["%s"]' % key
            if type(json_data[key]) not in [type({}), type([])]:  # key对应的value值既不是数组，也不是字典
                data_struct_list.append(temp_data_struct_link)

            else:
                parse_json(json_data[key], temp_data_struct_link,data_struct_list)

    elif type(json_data) == type([]):  # 数组类型
        array_length = len(json_data)
        for index in range(0, array_length):
            temp_json_data = json_data[index]
            # 判断列表是否能转化成字段
            # if '{' in str(temp_json_data):
            if type(json_data) == type({}):
                keys_list = temp_json_data.keys()

                for key in keys_list:
                    temp_data_struct_link = data_struct_link + '[%s]["%s"]' % (str(index), key)

                    if type(temp_json_data[key]) not in [type({}), type([])]:  # key对应的value值既不是数组，也不是字典
                        data_struct_list.append(temp_data_struct_link)

                    else:
                        parse_json(temp_json_data[key], temp_data_struct_link)
            else:
                temp_data_struct_link = data_struct_link + '[%s]["%s"]' % (str(index), temp_json_data)
                data_struct_list.append(temp_data_struct_link)

def seekKey(json_data, dateStruct, key,date):
    if isinstance(json_data, dict) or isinstance(json_data, list):
        for keyText in dateStruct:
            if key not in str(keyText):
                continue
            flag1 = bool(re.search(r'\[\"{key}\"\]'.format(key=key), keyText))
            flag2 = bool(re.search(r"\[\'{key}\'\]".format(key=key), keyText))
            if not (flag1 or flag2):
                continue
            # flag = bool(re.search(r'\[\d\]', keyText))
            # if flag:
            #     pattern1 = r'\[\d\]'
            #     pattern2 = r'"|\''
            #     b1 = re.split(pattern1, keyText)
            #     b2 = re.split(pattern2, b1[-2])
            #     if b2[-2] == key:
            #         # pass
            #         c = keyText[0:keyText.index(b2[-2]) - 2]
            #         targe = eval(c)
            #         targe[key] = date
            # else:
            #     # pattern = r'"|\''
            #     # b = re.split(pattern, keyText)
            #     b1 = keyText.split(key)
            #     if len(b1) >= 2:
            #         # c = keyText[0:keyText.index(b[-2]) - 2]
            #         c1 = keyText[0:len(b1[0])-2]
            #         targe = eval(c1)
            #         targe[key] = date

            b1 = keyText.split(key)
            if len(b1) >= 2:
                # c = keyText[0:keyText.index(b[-2]) - 2]
                # c1 = keyText[0:len(b1[0]) - 2]
                c1 = keyText[0:len(b1[0]) - 2]
                try:
                    targe = eval(c1)
                    targe[key] = date
                except Exception as e:
                    print(e)

    return json_data

if __name__ == '__main__':
    json_data =  {
    "name": "11111",
    "tagsID": [
        5,
        4
    ],
    "tags": [
        "MongoDB",
        "SQLServer"
    ],
    "agent": "AR-Agent",
    "category": "FileCollect",
    "schedule": {
        "type": "timequantum",
        "intervalTime": "10s",
        "period": "day",
        "days": 1,
        "startTime": "01:00",
        "endTime": "04:00"
    },
    "configInputTemplateIds": [
        "aef3bbb0-a951-11ea-af9f-0242ac120007"
    ],
    "configOutputTemplateIds": [],
    "configGroupIds": [
        "5bc74cd8-a968-11ea-af9f-0242ac120007"
    ],
    "configHostIds": [],
    "description": ""
}
    # print(json_data)

    data_struct_list = []  # 用于存放所有 json 元素路径，形如 json_data[0]["data"][0]["components"][0]["enabled"]
    data_struct_link = 'json_data'  # 用于临时存放单条json元素路径


    parse_json(json_data, data_struct_link,data_struct_list)
    print(data_struct_list)

    date = 'abcd'
    date = seekKey(json_data, data_struct_list, 'endTime',date)
    print(date)

