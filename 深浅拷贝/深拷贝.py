#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 11:17
# @Author   : 洪松
# @File     : 深拷贝.py

'''
深拷贝相当于克隆了一份
'''
import copy

message_1 = ['yangyang',123,[5,6,7]]
print(message_1)
message_2 = copy.deepcopy(message_1)
print(message_2)

message_2[2][0] = 'hongsong'
message_2[1] = 456
print("message_1:", message_1)
print("message_2:", message_2)