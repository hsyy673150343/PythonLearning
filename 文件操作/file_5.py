#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 11:20
# @Author   : 洪松
# @File     : file_5.py

'''

with方法:会自动关闭文件

'''

with open('小重山山','r',encoding='utf-8') as file:
    print(file.read())
