#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 9:09
# @Author  : Evan.hu

import requests
import json

url = "http://192.168.84.35/v1/search/fieldsAggs"
url_get= "http://192.168.84.35/api/v1/dataManager/logWareHouse?page=-1&size=-1&order=createTime&by=DESC"

payload = {
    "filters": {
        "must": [
            {
                "query_string": {
                    "analyze_wildcard": True,
                    "auto_generate_phrase_queries": True,
                    "query": "*"
                }
            }
        ]
    },
    "indices": {
        "indexPattern": [],
        "manualIndex": []
    },
    "aggFields": [
        "host.keyword",
        "_type",
        "tags.keyword"
    ]
}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url_get, headers=headers)  #, data = json.dumps(payload)

print(response.json())
