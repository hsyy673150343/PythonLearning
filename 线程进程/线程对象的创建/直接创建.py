#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/17 16:45
# @Author   : 洪松
# @File     : 直接创建.py

import threading
import time

def countNum(n): # 定义某个线程要运行的函数

    print("running on number:%s" %n)

    time.sleep(3)

if __name__ == '__main__':

    t1 = threading.Thread(target=countNum,args=(23,)) #生成一个线程实例
    t2 = threading.Thread(target=countNum,args=(34,))

    t1.start() #启动线程
    t2.start()

    print("ending!")