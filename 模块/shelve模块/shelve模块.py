#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:48
# @Author   : 洪松
# @File     : shelve模块.py

'''
shelve模块比pickle模块简单，只有一个open函数，
返回类似字典的对象，可读可写;Key必须为字符串，而值可以是python所支持的数据类型
'''

import shelve

f = shelve.open('shelve_test')

f['info'] = {'name':'liling','age':'56'}
f['shopping'] = {'name':'cake','price':'20'}

data_1 = f.get('info')
print(data_1)#{'name': 'liling', 'age': '56'}

data_2 = f['shopping']
print(data_2)#{'name': 'cake', 'price': '20'}