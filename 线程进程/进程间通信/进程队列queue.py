#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/20 18:32
# @Author   : 洪松
# @File     : 进程队列queue.py


from multiprocessing import Process, Queue

def f(q):
    q.put([42, 2, 'hello'])
    print('subprocess a id:',id(q))


if __name__ == '__main__':
    q = Queue()#创建进程队列对象
    p_list = []
    print('main a id:',id(q))


    for i in range(3):
        p = Process(target=f,args=(q,))
        p_list.append(p)
        p.start()

    print(q.get())
    print(q.get())
    print(q.get())

    for i in p_list:
        i.join()