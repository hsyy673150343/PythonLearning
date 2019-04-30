#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:21
# @Author   : 洪松
# @File     : 迭代器_2.py

from collections.abc import Iterator,Iterable

'''
Py西游攻关
'''

'''
可以使用isinstance()判断一个对象是否是Iterator(迭代器)对象
'''
li = [1,2,3,4]
d = iter(li)#iter方法，返回一个迭代器对象
print(d)#<list_iterator object at 0x000001A0754041D0>
print(isinstance(li,list))#True
print(isinstance(li,Iterable))#True
print(isinstance(li,Iterator))#False
print(isinstance(d,Iterator))#True
