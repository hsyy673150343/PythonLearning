#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/19 20:12
# @Author   : 洪松
# @File     : 队列.py

# import queue
#
#
# d = queue.Queue(2)#'''先进先出  FIFO'''
#
# d.put('yy')
# d.put('hs')
# d.put('haha')
#
# print(d.get())
# print(d.get())



import threading,queue
from time import sleep
from random import randint

class Production(threading.Thread):
    def run(self):
        while True:
            r=randint(0,100)
            q.put(r)
            print("生产出来%s号包子"%r)
            sleep(1)
class Proces(threading.Thread):
    def run(self):
        while True:
            re=q.get()
            print("吃掉%s号包子"%re)
if __name__=="__main__":
    q=queue.Queue(10)
    threads=[Production(),Production(),Production(),Proces()]
    for t in threads:
        t.start()