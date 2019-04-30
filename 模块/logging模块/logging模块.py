#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:44
# @Author   : 洪松
# @File     : logging模块.py

import logging


# logging.debug('杨洋是个瓜娃子')
# logging.warning('羊羊羊')
# logging.info('杨洋是个大瓜娃子')

# logging.basicConfig(level=logging.DEBUG)#改变默认的日志级别
# logging.debug('杨洋是个瓜娃子')
# logging.warning('羊羊羊')
# logging.info('杨洋是个大瓜娃子')

'''
将日志保存到文件
'''
# logging.basicConfig(level=logging.DEBUG,filename='hongsong_code.log',filemode='test_before')
# logging.debug('杨洋是个瓜娃子')
# logging.warning('羊羊羊')
# logging.info('杨洋是个大瓜娃子')

'''
format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
'''
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%test_before, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='w')

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')