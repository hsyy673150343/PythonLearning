#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:24
# @Author   : 洪松
# @File     : pickle_loads.py

#***********反序列化***********#
import pickle

def foo():
    print('ok')

f = open('pickle_test','rb')

data_1 = f.read()
data_2 = pickle.loads(data_1)

data_2()
