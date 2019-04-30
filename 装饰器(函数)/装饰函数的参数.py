#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:00
# @Author   : 洪松
# @File     : 装饰函数的参数.py

import time
def logger(flag):
    def show_time(func):
        def inner(*x,**y):
            start = time.time()
            func(*x,**y)
            before = time.time()
            print('%s' % (before - start))
            if flag == 'true':
               print('日志记录')
        return inner
    return show_time

@logger('true')#相当于@show_time
def add(*a,**b):
    sum = 0
    for i in a:
        sum += i
    print(sum)
    time.sleep(1)
add(1,2,3,4,5,6)

@logger('flase')
def bar():
    print('bar..')
    time.sleep(3)
bar()