#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 17:19
# @Author   : 洪松
# @File     : 元类.py

'''Python中一切事物皆是对象'''


# class Foo:
#     pass
#
# obj = Foo()
'''
obj是对象
Foo类也是一个对象，type的对象

类都是type类的对象  type(...)
"对象"都是类的对象  类()
'''

# class MyType(type):
#     def __init__(self,*args,**kwargs):
#         print(123)
#         pass
#
# class Foo(object,metaclass=MyType):
#     '''不用type去创建类，用MyType去创建类'''
#     def func(self):
#         print('hello wupeiqi')
#输出:123






# class MyType(type):
#     '''MyType里的self是指Foo类'''
#     def __init__(self,*args,**kwargs):
#         print(123)
#         pass
#     def __call__(self, *args, **kwargs):
#         # print(456)
#        r = self.__new__(self, *args, **kwargs)
#        self.__init__(obj)
#
# class Foo(object,metaclass=MyType):
#     '''不用type去创建类，用MyType去创建类---
#     Foo是MyType的对象'''
#     def __init__(self,*args,**kwargs):
#         pass
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls,*args,**kwargs)
#
#
#
# #obj其实是在new里边创建的
# obj = Foo()#先执行MyType的init方法；再执行call方法

# 输出：123
#       456


class MyType(type):

    def __init__(self, what, bases=None, dict=None):
        super(MyType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        obj = self.__new__(self, *args, **kwargs)

        self.__init__(obj)

class Foo(object,metaclass=MyType):

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)

# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象
obj = Foo()