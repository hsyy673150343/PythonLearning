#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/13 21:32
# @Author   : 洪松
# @File     : code.py

'''
py3---->只有两种数据类型：str和bytes
   ---->str:Unicode编码
   ----》bytes:十六进制
'''


s = 'hello洪松'
print(type(s))#<class 'str'>


'''str---->bytes：编码'''
#方法一
b1 = bytes(s,'utf-8')#utf-8里一个汉字占3个字节
print(b1)#b'hello\xe6\xb4\xaa\xe6\x9d\xbe'  #utf-8规则下的bytes类型
#方法二
b2 = s.encode('utf-8')
print(b2)#b'hello\xe6\xb4\xaa\xe6\x9d\xbe'  #utf-8规则下的bytes类型

b3 = s.encode('gbk')#gbk里一个汉字占2个字节
print('gbk编码下的bytes数据：',b3)


'''按什么规则编码就按什么规则解码'''



'''bytes---->str:解码'''
s1 = str(b2,'utf-8')
print(s1)#hello洪松  #str类型

s2 = b2.decode('utf-8')
print(s2)#hello洪松  #str类型

s3 = b3.decode('gbk')
print(s3)