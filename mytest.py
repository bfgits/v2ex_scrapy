#!/usr/bin/env python
#-*- coding: UTF-8 -*-
'''
@File  : check_id.py
@Author: Simon Zhu
@Date  : 25/4/2019 6:02 PM
@Desc  :
'''

import requests

def hello():
    res = requests.get("https://httpbin.org/get")
    print(res.status_code)
    print(res.text)
    print("hello world")

if __name__ == '__main__':
    hello()
