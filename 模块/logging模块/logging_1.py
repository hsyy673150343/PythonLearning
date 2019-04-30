#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:55
# @Author   : 洪松
# @File     : logging_1.py

import logging



logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test_1.log')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
logger.addHandler(ch)

logger.setLevel(logging.DEBUG)


logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')