#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/16 15:50
# @Author   : 洪松
# @File     : threading.py


'''
线程（英语：thread）是操作系统能够进行运算调度的最小单位。
它被包含在进程之中，是进程中的实际运作单位。
一条线程指的是进程中一个单一顺序的控制流，
一个进程中可以并发多个线程，每条线程并行执行不同的任务。
'''


import time
import threading

begin = time.time()

def foo(n):
    print('foo %s' % n,end='\n')
    time.sleep(2)#sleep的状态是不占CPU的
    print('end foo')

def bar(n):
    print('bar %s' % n,end='\n')
    time.sleep(2)
    print('end bar')

# foo()
# bar()

t1 = threading.Thread(target=foo,args=(1,))#创建了一个线程对象
t2 = threading.Thread(target=bar,args=(2,))#创建了一个线程对象
t1.start()
t2.start()

print('....in the main....')

'''时间很短的原因是：在主线程里只进行了计算开始的时间和创建两个线程以及计算结束的时间'''
# end = time.time()
# print(end - begin)#0.0014483928680419922

t1.join()
t2.join()
end = time.time()
print(end-begin)#2.0023157596588135

'''
A thread is an execution context, which is all the information a CPU needs to execute a stream of instructions.
一个线程就是一堆指令集合，
'''
