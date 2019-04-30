#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:39
# @Author   : 洪松
# @File     : time模块.py

import time

'''
时间戳、结构化时间、格式化时间
'''
# print(help(time))

# print(time.time())#1547282818.1377523：时间戳 ******
# # time.sleep(3) # ******
#
# print(time.clock())#计算CPU执行时间 will be removed from Python 3.8
#
# #结构化时间
# print(time.gmtime(0))#time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
# print(time.gmtime())#time.struct_time(tm_year=2019, tm_mon=1, tm_mday=12, tm_hour=9, tm_min=4, tm_sec=9, tm_wday=5, tm_yday=12, tm_isdst=0)
#
# print(time.localtime())#time.struct_time(tm_year=2019, tm_mon=1, tm_mday=12, tm_hour=17, tm_min=6, tm_sec=17, tm_wday=5, tm_yday=12, tm_isdst=0)
#
#
# struct_time = time.localtime()
# print(time.strftime('%Y-%m-%d %H:%M:%S',struct_time)) #默认当前时间
#
#
# print(time.strptime('2019-01-13 13:22:39','%Y-%m-%d %H:%M:%S')) #结构化将其转化为元组******
# #time.struct_time(tm_year=2019, tm_mon=1, tm_mday=13, tm_hour=13, tm_min=22, tm_sec=39, tm_wday=6, tm_yday=13, tm_isdst=-1)
#
# test_before = time.strptime('2019-01-13 13:22:39','%Y-%m-%d %H:%M:%S')
# print(test_before.tm_year)
# print(test_before.tm_mday)
# print(test_before.tm_wday)
#
# print(time.ctime())#获取本地时间
# print(time.ctime(1547282818.1377523))#将时间戳转换为当前时间
#
#
#
# # print(help(time.mktime))#This is the inverse function of localtime()
# print(time.mktime(time.localtime()))#1547357881.0  将本地时间转换为时间戳



import datetime
print(datetime.datetime.now())
