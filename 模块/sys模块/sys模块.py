#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 15:23
# @Author   : 洪松
# @File     : sys模块.py

'''
与python解释器进行交互 ----在cmd窗口运行程序
'''

import sys

print(sys.argv)

def post():
    print('hongsong')

def download():
    print('yangyang')

if sys.argv[1] == 'past':
    post()

if sys.argv[1] == 'path':
    download()

# import time
# print(sys.path)#返回模块的搜索路径


print(sys.platform)#返回操作系统平台名称