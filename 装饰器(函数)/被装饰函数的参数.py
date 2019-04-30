#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 15:39
# @Author   : 洪松
# @File     : 被装饰函数的参数.py
import time

def show_time(func):
    def inner(*x,**y):
        start = time.time()
        func(*x,**y)
        before = time.time()
        print('%s' % (before - start))
    return inner

@show_time #相当于add = show_time(add)
def add(*a,**b):
    sum = 0
    for i in a:
        sum += i
    print(sum)
    time.sleep(1)

add(1,2,5,7)
