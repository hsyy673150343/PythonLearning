#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:02
# @Author   : 洪松
# @File     : function_6.py
'''
高阶函数---->函数名可以作为参数输入
       ---->函数名可以作为返回值
'''
# def f(n):
#     return n*n
#
# def foo(test_before,b,func):
#     ret = func(test_before) + func(b)
#     return ret
#
# print(foo(1,2,f))


'''
递归函数---->调用自身函数
       ---->有一个结束条件
       ---->每次进入更深一层递归时，问题规模相比上次递归都应有所减少
但凡能用递归解决的问题，循环都能解决
***递归的效率在很多时候会很低，递归层次过多会导致栈溢出
'''
# def digui(n):
#     test_before = 1
#     for i in range(2,n+1):
#         test_before = test_before * i
#     return test_before
# print(digui(5))

# def digui_1(n):
#     if n==1:
#         return 1
#     return n * digui_1(n-1)
# print(digui_1(5))

'''
求阶乘简便方法 5!
'''
from functools import reduce
result = reduce(lambda x,y : x*y, range(1,6))
print(result)

'''
斐波那契数列0 1 1 2 3 5 8 13 21 34 55
'''
def fibo(n):

    if n==0 or n==1:
        return n

    return fibo(n-1) + fibo(n-2)
print(fibo(8))