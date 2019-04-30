#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:49
# @Author   :洪松
# @File     :file_3.py
'''
r+,w+,test_before+
'''

# file_1 = open('测试','r+',encoding='utf-8')#可读(光标在起始位置)，可写(在文件最后写入内容)
# print(file_1.readline())
# file_1.write('杨洋')
#
# file_2= open('测试','w+',encoding='utf-8')#可读，可写,但要格式化文件后，再写入内容
# print(file_2.readline())
# file_2.write('洪松')#写入内容后，光标就跑到最后了，如果再读取文件里的内容，什么都读取不到
# # print(file_2.readline())
# print(file_2.tell())#6
# file_2.seek(0)#调整光标到文件起始位置
# print(file_2.readline())#这个时候读取文件才能读取到内容
# file_2.close()

file_3 = open('测试','test_before+',encoding='utf-8')#可读(光标在最后)，可写(在文件最后追加内容)
print(file_3.tell())
file_3.seek(0)
print(file_3.readline())