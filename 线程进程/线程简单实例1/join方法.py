#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/16 17:29
# @Author   : 洪松
# @File     : join方法.py


'''
IO密集型任务或函数
计算密集型任务函数
'''


'''
Python GIL(Global Interpreter Lock)　
CPython implementation detail: In CPython, due to the Global Interpreter Lock, only one thread can execute Python code at once.
CPython实现细节：在CPython中，由于Global Interpreter Lock，在同一时刻，只能有一个线程可以执行Python代码。

无论你启多少个线程，你有多少个cpu, Python在执行一个进程的时候会淡定的在同一时刻只允许一个线程运行。
所以，python是无法利用多核CPU实现多线程的。

协程+多进程

结论：在python里：如果任务是IO密集型的，可以用多线程
                 如果是计算密集型的---》改用C
'''
import threading
import time

begin = time.time()
def add(n):
    sum = 0
    for i in range(n):
        sum += i
    print(sum)
#
add(100000000)
add(100000000)
end = time.time()
print(end-begin)#8.917975187301636

# t1 = threading.Thread(target=add,args=(100000000,))
# t1.start()
#
# t2= threading.Thread(target=add,args=(10000000,))
# t2.start()
#
# t1.join()
# t2.join()
#
# end = time.time()
# print(end-begin)#4.615864276885986