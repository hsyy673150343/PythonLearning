#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:03
# @Author   : 洪松
# @File     : random模块.py

import random

# print(random.random())

# print(random.randint(1,8))#包括8

# print(random.choice([1,'123',[4,5,6]]))#从非空序列seq返回一个随机元素。如果seq为空，则加注IndexError

# print(random.randrange(1,3))

'''
生成伪随机码
'''
def v_code():
    code = ''
    for i in range(5):
        add = random.choice([random.randrange(10),chr(random.randrange(65,91))])
        code += str(add)
    print(code)
v_code()