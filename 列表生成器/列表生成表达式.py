#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:48
# @Author   : 洪松
# @File     : 列表生成表达式.py

def func(n):
    return n**3

a = [func(x) for x in range(10)]

print(a)
print(type(a))