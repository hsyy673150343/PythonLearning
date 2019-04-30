#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:59
# @Author   : 洪松
# @File     : hashlib模块.py

import hashlib

'''
3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
'''

# m = hashlib.md5()
# print(m)
#
# m.update('hello world'.encode('utf-8'))#update()不支持将字符串对象引入，因为哈希在字节上工作，而不在字符上工作。
# print(m.hexdigest())#5eb63bbbe01eeed093cb22bb8f5acdc3
#
# m.update('hongsong'.encode('utf-8'))
# print(m.hexdigest())#6fe6842211501f1a90700d73ab7f33d9
#
# m2 = hashlib.md5()
# m2.update('hello worldhongsong'.encode('utf-8'))
# print(m2.hexdigest())#6fe6842211501f1a90700d73ab7f33d9


s = hashlib.sha1()
s.update('hongsong'.encode('utf8'))
print(s.hexdigest())