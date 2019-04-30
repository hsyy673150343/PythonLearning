#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/17 17:13
# @Author   : 洪松
# @File     : pil.py


import time
import threading

def addNum():
    global num #在每个线程中都获取这个全局变量
    # num-=1
    L.acquire()
    temp = num
    time.sleep(0.0001)
    num = temp - 1
    L.release()

num = 100  #设定一个共享变量

thread_list = []

L = threading.Lock()

for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list: #等待所有线程执行完毕
    t.join()

print('Result: ', num)