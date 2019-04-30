#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:14
# @Author   : 洪松
# @File     : json_loads.py


import json
#******反序列化**********#
f = open('json_test','r')

'''json.loads()'''
# data_1 = f.read()
# data_2 = json.loads(data_1)
# print(data_2['name'])

'''json.load()'''
data = json.load(f)
print(data['name'])



data = json.loads(f.read())
print(data['name'])
