#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 17:41
# @Author   : 洪松
# @File     : 装饰器.py

import time

'''
遵守开放封闭原则
'''


# def foo():
#     print('foo..')
#     time.sleep(2)
#
# def bar():
#     print('foo..')
#     time.sleep(3)


# def show_time(func):
#     start = time.time()
#     func()
#     before = time.time()
#     print('%s' % (before - start))
#
# show_time(foo)


'''
装饰器函数
'''

def show_time(func):
    def inner():
        start = time.time()
        func()
        before = time.time()
        print('%s' % (before - start))
    return inner

@show_time #相当于foo = show_time(foo)
def foo():
    print('foo..')
    time.sleep(2)

@show_time #相当于bar = show_time(bar)
def bar():
    print('bar..')
    time.sleep(3)

# foo = show_time(foo)
foo()#实际上是执行的inner函数!!!!

# bar = show_time(bar)
bar()


