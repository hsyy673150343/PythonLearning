#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/19 18:46
# @Author   : 洪松
# @File     : xinhaoliang.py


import threading,time

class myThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(3)
            semaphore.release()



if __name__=="__main__":
    semaphore = threading.BoundedSemaphore(5)
    thrs = []
    for i in range(10):
        thrs.append(myThread())
    for t in thrs:
        t.start()