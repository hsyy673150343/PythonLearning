#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 20:03
# @Author   : 洪松
# @File     : s3.py

import s2
inp = input('请输入要查看的URL')

if hasattr(s2,inp):

    func = getattr(s2,inp)
    print(func())
else:
    print('用户输入错误')