#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 17:26
# @Author   : 洪松
# @File     : file_4.py

'''

修改磁盘文件

'''

# file_1 = open('小重山','r',encoding='utf-8')
# file_2 = open('小重山山','w',encoding='utf-8')
with open('小重山','r',encoding='utf-8') as file_1, open('小重山山','w',encoding='utf-8') as file_2:
    number = 0
    for line in file_1:
        number += 1
        if number == 6:
            file_2.write('yangyang\n')
        else:
            file_2.write(line)

