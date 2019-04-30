#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:56
# @Author   : 洪松
# @File     : function_4.py

'''
变量的修改---如果在函数内部要修改全局变量，必须在要修改的变量前加global
'''
# count = 10
# def outer():
#     print(count)#local variable 'count' referenced before assignment
#     count = 5

# def outer():
# #     global count
# #     print(count)
# #     count = 5
# #     print(count)
# #
# # outer()

'''
函数嵌套的时候，如果要在内层函数修改外层函数变量的值，必须在要修改的局部变量前加nonlocal
'''
def outer():
    count = 10
    def inner():
        nonlocal count
        count = 20
        print(count)
    inner()
    print(count)
outer()

'''
小结：
(1)变量查找顺序：LEGB
(2)只有模块、类、及函数才能引入新作用域
(3)对于一个变量，内部作用域先声明就会覆盖外部变量，不声明直接使用，就会使用外部作用域的变量
(4)内部作用域要修改外部作用域变量的值时，全局变量要使用global关键字，嵌套作用域变量要使用nonlocal关键字
nonlocal关键字是python3新增的关键字，有了这个关键字，就能完美的实现闭包了。
'''