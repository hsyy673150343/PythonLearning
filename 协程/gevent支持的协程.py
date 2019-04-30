#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/20 21:05
# @Author   : 洪松
# @File     : gevent支持的协程.py

'''import gevent
import time

def foo():
    print("running in foo")
    gevent.sleep(2)
    print("switch to foo again")

def bar():
    print("switch to bar")
    gevent.sleep(5)
    print("switch to bar again")

start=time.time()

gevent.joinall(
    [gevent.spawn(foo),
    gevent.spawn(bar)]
)

print(time.time()-start)
'''


from gevent import monkey
monkey.patch_all()
import gevent
from urllib import request
import time

def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

start=time.time()

gevent.joinall([
        gevent.spawn(f, 'https://itk.org/'),
        gevent.spawn(f, 'https://www.github.com/'),
        gevent.spawn(f, 'https://zhihu.com/'),
])
print(time.time()-start)
