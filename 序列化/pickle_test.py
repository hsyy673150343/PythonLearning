#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:20
# @Author   : 洪松
# @File     : pickle_test.py


#*******序列化************#
import pickle

def  foo():
    print('ok')

data = pickle.dumps(foo)
f = open('pickle_test','wb')

f.write(data)
f.close()