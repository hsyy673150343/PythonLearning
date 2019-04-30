#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/19 19:52
# @Author   : 洪松
# @File     : tongbutiaojian.py


import threading,time

class Boss(threading.Thread):
    def run(self):
        print("BOSS：今晚大家都要加班到22:00。")
        event.isSet() or event.set()
        time.sleep(5)
        print("BOSS：<22:00>可以下班了。")
        event.isSet() or event.set()
class Worker(threading.Thread):
    def run(self):
        event.wait()
        print("Worker：哎……命苦啊！")
        time.sleep(1)
        event.clear()
        event.wait()
        print("Worker：OhYeah!")
if __name__=="__main__":
    event = threading.Event()
    threads = []
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()