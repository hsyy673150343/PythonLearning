#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/20 20:15
# @Author   : 洪松
# @File     : yield实现协程操作.py


import time

def consumer(name):
    print("--->starting....")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name, new_baozi))
        time.sleep(1)


def producer():
    next(con1)
    next(con2)
    n = 0
    while n < 5:
        n += 1
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
        con1.send(n)
        con2.send(n)

if __name__ == '__main__':
    con1 = consumer("c1")#创建一个生成器对象
    con2 = consumer("c2")#创建一个生成器对象
    p = producer()