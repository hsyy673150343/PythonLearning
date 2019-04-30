#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:59
# @Author   : 洪松
# @File     : 生成器_2.py

def bar():
    print('ok1')
    a = yield 1
    print(a)

    # print('ok')
    yield 2

b = bar()
'''
第一次send前如果没有next,只能传一个send(None)。
第二次send时，会从上次返回的yield语句处继续执行，
所以第二次send时就把值传给了a
'''
s = b.send(None)#相当于next(b)
print(s)

s = b.send('yangyang')