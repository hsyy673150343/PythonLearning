#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 15:23
# @Author   : 洪松
# @File     : function_1.py

import time

# time_format = '%Y-%m-%d %X'
# time_current = time.strftime(time_format)
# print(time_current)

def logger(n):
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('日志记录.txt','test_before') as f:
        f.write('%s end operation%s\n' %(time_current,n))

def action_1(n):
    print('starting action_1...')
    logger(n)

def action_2(n):
    print('starting action_2...')
    logger(n)

def action_3(n):
    print('starting action_3...')
    logger(n)

action_1(1)
action_2(2)
action_3(3)