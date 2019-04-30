#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 17:55
# @Author   : 洪松
# @File     : s1.py

class Foo:

    def __init__(self,name,age):
        self.n = name
        self.a = age
    def show(self):
        return '%s-%s' % (self.n,self.a)

obj = Foo('hongsong',24)
# print(obj.__dict__['n'])#hongsong


'''
通过字符串的形式操作对象中的成员
'''

'''getattr()---获取成员'''
#print(getattr(obj,'n'))#hongsong

# inp = input('>>>')
# v = getattr(obj,inp)
# print(v)

# func = getattr(obj,'show')
# print(func)#<bound method Foo.show of <__main__.Foo object at 0x0000023DAA073550>>
#
# r = func()
# print(r)#hongsong-24


'''
hasattr()---判断对象里检查是否含有成员
setattr()---检查是否含有成员
delattr()---删除成员
'''

# setattr(obj, 'a', 18)
# print(obj.a)
#
# delattr(obj,'n')
# print(obj.n)'Foo' object has no attribute 'n'


# class Foo:
#     stat = '123'
#
#     def __init__(self,name,age):
#         self.n = name
#         self.a = age
# #通过字符串的形式操作对象中的成员
# r = getattr(Foo,'stat')
# print(r)

#s1.py

import s2

r1 = s2.NAME
print(r1)#hongsong
r2 = s2.func()
print(r2)#func

r1 = getattr(s2,'NAME')
print(r1)#hongsong

r2 = getattr(s2,'func')
print(r2)
print(r2())

cls = getattr(s2,'Foo')
print(cls)
obj = cls('123')
print(obj.n)