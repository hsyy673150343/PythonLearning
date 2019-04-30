#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/19 19:01
# @Author   : 洪松
# @File     : 条件变量.py

# import threading,time
# from random import randint
#
#
# class Producer(threading.Thread):
#     def run(self):
#         global L
#         while True:
#             val = randint(0,100)
#             print('生产者',self.name,":Append"+str(val),L)
#             if lock_con.acquire():
#                 L.append(val)
#                 lock_con.notify()
#                 lock_con.release()
#             time.sleep(3)
# class Consumer(threading.Thread):
#     def run(self):
#         global L
#         while True:
#                 lock_con.acquire()
#                 if len(L)==0:
#                     lock_con.wait()
#                 print('消费者',self.name,":Delete"+str(L[0]),L)
#                 del L[0]
#                 lock_con.release()
#                 time.sleep(0.25)
#
# if __name__=="__main__":
#
#     L = []
#     lock_con = threading.Condition()
#     threads = []
#     for i in range(5):
#         threads.append(Producer())
#     threads.append(Consumer())
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
#     print('---------------')

import threading
import time

class Producer(threading.Thread):
    def run(self):
        global count
        while True:
            if lock_con.acquire():
                if count > 1000:
                    lock_con.wait()
                else:
                    count = count+100
                    msg = self.name+' produce 100, count=' + str(count)
                    print(msg)
                    lock_con.notify()
                    lock_con.release()
                time.sleep(1)


class Consumer(threading.Thread):
    def run(self):
        global count
        while True:
            if lock_con.acquire():
                if count < 100:
                    lock_con.wait()
                else:
                    count = count-3
                    msg = self.name+' consume 3, count='+str(count)
                    print(msg)
                    lock_con.notify()
                    lock_con.release()
                time.sleep(1)


count = 500
lock_con = threading.Condition()


def test():
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
if __name__ == '__main__':
    test()