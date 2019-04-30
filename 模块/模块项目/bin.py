#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:17
# @Author   : 洪松
# @File     : bin.py

# import sys
'''
解释器通过搜索路径找到calculate.py后，将calculate.py里的所有代码全给了calculate
'''
# import calcul

# print(calculate.add(1,2))

#搜索路径 sys.path
# print(sys.path)

# print(calculate.x)


'''
从模块里加载方法
'''
# from calculate import add,sub
#
# print(add(1,4))
# print(sub(3,6))

'''
然而这种声明不该被过多地使用。大多数情况， Python程序员不使用这种方法，
因为引入的其它来源的命名，很可能覆盖了已有的定义。
'''
# def add(x,y):
#     return x+y+2
#
# from calculate import *
#
# print(add(1,4))
# print(sub(3,6))


# import web.logger#错
# logger.logger()#name 'logger' is not defined

# from web.web2 import logger
# logger.logger()

# from web.web2.logger import logger
# # logger()


import web  #执行了__init__文件

from web import  main