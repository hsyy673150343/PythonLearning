#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 15:41
# @Author   : 洪松
# @File     : funcation_5.py

'''
函数名可以进行赋值，
函数名可以作为函数参数，还可以作为函数的返回值
'''
# def f():
#     print('ok')
#
# foo = f


# def bar(test_before,b,func):
#     func()
#     return 1
# bar(1,2,f)


# def foo_1():
#     def foo_2():
#         return 88
#     return foo_2
# print(foo_1())#<function foo_1.<locals>.foo_2 at 0x00000216F872A840>


def foo_1():
    def foo_2():
        return 88
    return foo_2
a = foo_1()
print(a())#88