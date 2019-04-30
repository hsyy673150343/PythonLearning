#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 17:26
# @Author   :洪松
# @File     :file_1.py
# import time

# file = open('小重山','r',encoding='utf-8')
# data = file.read()#一个字符一个字符的读
# print(data)
# file.close()
#
# file_2 = open('小重山2','test_before',encoding='utf-8')
# file_2.write('杨洋是个傻瓜')

# time.sleep(20)


file_1 = open('小重山','r',encoding='utf-8')
# message = file_1.readlines()#message的类型是list,数据全部放到内存里了,注意及时关闭文件
number = 0
for data in file_1:
    number += 1
    # if number==6:
    #     print(data.strip(),"hongsong")
    # else:
    #     print(data.strip())
    if number == 6:
        # data = data.strip() + 'hongsong'
        data = ''.join((data.strip(),"hongsong"))
        # data = ''.join(data.strip() + "hongsong")
    print(data.strip())



# data1 = file_1.readline()
# print(data1)
# data2 = file_1.readline()
# print(data2)
# data3 = file_1.readlines()
# print(data3)
# print(type(data3))#list 列表类型

