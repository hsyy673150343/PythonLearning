#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 15:40
# @Author   : 洪松
# @File     : 迭代器_1.py

'''
生成器都是迭代器，迭代器不一定是生成器
迭代器满足两个条件：
--->有iter方法
--->有next方法
'''

'''
我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象
'''



# li = [1,2,3,4]
# d = iter(li)#iter方法，返回一个迭代器对象
# print(d)#<list_iterator object at 0x00000145ED434DD8>
#
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))

# print(next(d))#StopIteration

'''
for 循环内部三件事：
--->调用可迭代对象的iter方法返回一个迭代器对象
--->不断调用迭代器对象的next方法
--->处理StopIteration
'''

# s = 'hsyy'
# for char in s:
#     print(char)


s = 'hsyy'
it = iter(s)#使用可迭代对象构建迭代器it
while True:
    try:
        print(next(it))#不断在迭代器上调用next函数，获取下一个字符。
    except StopIteration:#如果没有字符了，迭代器会抛出StopIteration异常。
        del it#释放对it的引用，即废弃迭代器对象。
        break#退出循环