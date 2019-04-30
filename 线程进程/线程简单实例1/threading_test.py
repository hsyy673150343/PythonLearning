#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/17 14:22
# @Author   : 洪松
# @File     : threading_test.py

# from time import ctime,sleep
# '''IO密集型，可以用多线程'''
# def music(func):
#     for i in range(2):
#         print('I was listening to %s. %s' % (func,ctime()))
#         sleep(1)
#
#
# def move(func):
#     for i in range(2):
#         print('I was at the %s! %s' % (func,ctime()))
#         sleep(5)
#
#
# if __name__ == '__main__':
#     music(u'七里香')
#     move(u'世界末路')



import threading
from time import ctime,sleep
import time

def music(func):
    for i in range(2):
        print ("Begin listening to %s. %s" %(func,ctime()),end='\n')
        sleep(4)
        print("end listening %s. %s" %(func,ctime()),end='\n')

def move(func):
    for i in range(2):
        print ("Begin watching at the %s! %s" %(func,ctime()),end='\n')
        sleep(5)
        print('end watching %s! %s' %(func,ctime()),end='\n')

threads = []
t1 = threading.Thread(target=music,args=('七里香',))
threads.append(t1)
t2 = threading.Thread(target=move,args=('阿甘正传',))
threads.append(t2)

if __name__ == '__main__':

    for t in threads:
        t.start()
    print ("all over %s" %ctime())