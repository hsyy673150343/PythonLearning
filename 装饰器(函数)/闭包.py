#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:30
# @Author   : 洪松
# @File     : 装饰器.py
'''
闭包:如果在一个内部函数里，对在外部作用域(但不是在全局作用域)的变量进行引用，那么内部函数就被认为是闭包closure。
'''

def outer():
     x = 10
     def inner():#条件一:inner就是内部函数

         print(x)#条件二：外部环境的一个变量

     return inner#结论： 内部函数inner就是一个闭包

# inner()#局部变量，全局无法调用

# outer()()#10

f = outer()
f()#10

