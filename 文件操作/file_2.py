#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 13:38
# @Author   :洪松
# @File     :file_2.py

'''
一般的文件流操作都包含缓冲机制，write方法并不直接将数据写入文件，而是先写入内存中特定的缓冲区。

flush方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区。

正常情况下缓冲区满时，操作系统会自动将缓冲数据写入到文件中。

至于close方法，原理是内部先调用flush方法来刷新缓冲区，再执行关闭操作，这样即使缓冲区数据未满也能保证数据的完整性。

如果进程意外退出或正常退出时而未执行文件的close方法，缓冲区中的内容将会丢失。

'''

# file_1 = open('小重山','r',encoding='utf-8')


# for i in file_1:#for循环内部将file_1对象组成一个迭代器，用一行取一行
#     print(i.strip())


# print(file_1.tell())
# print(file_1.read(2))
# print(file_1.tell())#tell---中文的时候默认一个中文占3个字符，一个英文字母占一个字符

#从起始位置开始
# file_1.seek(0)#seek(offset,where):where=0从起始位置移动，1从当前位置移动，2从结束位置移动。当有换行时，会被换行截断。seek（）无返回值，故值为None。
# print(file_1.read(4))

import sys,time
# for i in range(30):
#     # sys.stdout.write('*')#先是放到缓存区的
#     # sys.stdout.flush()
#     # time.sleep(0.2)
#
#     print('*',end='',flush=True)
#     time.sleep(0.2)

file_2 = open('测试','w',encoding='utf-8')#可写模式w下，不管对文件进行什么操作，首先要格式化文件
file_2.write('Hello World')
file_2.truncate(5)
print(file_2)

file_3 = open('截断','test_before',encoding='utf-8')
file_3.truncate(5)


