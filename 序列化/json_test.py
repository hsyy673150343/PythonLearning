#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:02
# @Author   : 洪松
# @File     : json_test.py

import json

'''
什么是序列化？
我们把对象(变量)从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
'''

#******序列化*****************#
'''json.dumps()'''
dic = {'name':'hongsong','age':'24'}

data = json.dumps(dic)
f = open('json_test','w')

f.write(data)
f.close()



# def  foo():
#     print('ok')
#
# #函数类型做不了序列化
# data = json.dumps(foo)#Object of type function is not JSON serializable
# f = open('json_test','w')
#
# f.write(data)
# f.close()

'''json.dump()'''

dic = {'name':'yangyang','age':'21'}
f = open('json_test_2','w')

json.dump(dic,f)#相比dumps，少了一步f.write,dump内部帮我们write
f.close()