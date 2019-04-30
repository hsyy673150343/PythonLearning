#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/19 21:42
# @Author   : 洪松
# @File     : 进程关系.py

from multiprocessing import Process
import os
import time
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello', name)

if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    time.sleep(10)
    p = Process(target=info, args=('bob',))
    p.start()
    p.join()