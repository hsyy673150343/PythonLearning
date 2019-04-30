#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/17 20:56
# @Author   : 洪松
# @File     : pil_1.py

import threading,time

class myThread(threading.Thread):
    def doA(self):
        lock.acquire()
        print(self.name,"A--gotlockA",time.ctime())
        time.sleep(3)
        lock.acquire()
        print(self.name,"A--gotlockB",time.ctime())
        lock.release()
        lock.release()

    def doB(self):
        lock.acquire()
        print(self.name,"B--gotlockB",time.ctime())
        time.sleep(2)
        lock.acquire()
        print(self.name,"B--gotlockA",time.ctime())
        lock.release()
        lock.release()
    def run(self):
        self.doA()
        self.doB()

if __name__ == "__main__":

    lock = threading.RLock()#递归锁

    threads=[]
    for i in range(5):
        threads.append(myThread())
    for t in threads:
        t.start()
    for t in threads:
        t.join()#等待线程结束，后面再讲。



