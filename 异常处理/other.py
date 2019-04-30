#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:23
# @Author   : 洪松
# @File     : other.py

'''一、isinstance(obj, cls)检查是否obj是否是类cls的对象
'''

class Foo(object):
    pass
obj = Foo()
print(isinstance(obj, Foo))#True

'''二、issubclass(sub, super)检查sub类是否是，super类的派生类
'''

class Foo(object):
    pass
class Bar(Foo):
    pass
print(issubclass(Bar, Foo))#True