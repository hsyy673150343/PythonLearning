#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/20 20:56
# @Author   : 洪松
# @File     : gevent下的协程.py


from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
