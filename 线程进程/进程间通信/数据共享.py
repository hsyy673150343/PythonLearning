#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/20 19:33
# @Author   : 洪松
# @File     : 数据共享.py


from multiprocessing import Process, Manager

def f(d, l,n):

    d[n] = n
    d["name"] ="alvin"
    l.append(n)

if __name__ == '__main__':

    with Manager() as manager:

        d = manager.dict()

        l = manager.list(range(5))

        p_list = []

        for i in range(10):
            p = Process(target=f, args=(d,l,i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)