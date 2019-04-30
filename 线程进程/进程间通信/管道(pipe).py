#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/20 19:20
# @Author   : 洪松
# @File     : 管道(pipe).py

from multiprocessing import Process, Pipe
import os

def f(conn):
    conn.send('小鱼是傻逼嘛？')#子进程发
    print(conn.recv(),'in the %s' % os.getpid())#子进程收
    conn.close()



if __name__ == '__main__':

    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()

    print(parent_conn.recv())#父进程收

    parent_conn.send('Hello')#父进程发
    p.join()
