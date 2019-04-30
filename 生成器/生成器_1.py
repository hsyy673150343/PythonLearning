#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 17:02
# @Author   : 洪松
# @File     : 生成器_1.py

'''
生成器有两种创建方式：
--->1. (x*2 for x in range(5))
--->2. yield

'''
# s = (x*2 for x in range(5))
# print(s)

# print(next(s))#等价于s.__next__()  in Py2: s.next()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

# print(next(s))#StopIteration

'''
生成器就是一个可迭代对象
'''
# for i in s:
#     print(i)



'''
通过yield来创建
'''

# def foo():
#     print('ok1')
#     yield 1
#
#     print('ok2')
#     yield 2
#
#
# g = foo()
# print(g)

# next(g)
# next(g)

# test_before = next(g)
# b = next(g)
# print(test_before,b)


# for i in foo():
#     print(i)

'''
什么是可迭代对象：对象拥有iter方法的可成为迭代对象
'''


'''
斐波那契数列 0 1 1 2 3 5 8 13 21.....
'''
# def fib(max):
#     n, before, after = 0, 0 ,1
#     while n < max:
#         # print(before)
#         yield before
#         before, after = after, before+after
#         n = n + 1
#
# for i in fib(10):
#     print(i)
#
# def foo():
#     yield 1
#     yield 2
#     yield 3
#
# for i in foo():
#     print(i)


# print(foo)
# print(foo())
# g = foo()
# print(next(g))
# print(next(g))
# print(next(g))


def Create_Generator():
    list  = range(3)
    for i in list:
        yield i*i

my_generator = Create_Generator()
print(my_generator)

for j in Create_Generator():
    print(j)