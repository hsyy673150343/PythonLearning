#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:15
# @Author   : 洪松
# @File     : 方法.py

'''
方法包括：普通方法、静态方法和类方法，三种方法在内存中都归属于类，区别在于调用方式不同。

普通方法：由对象调用；至少一个self参数；执行普通方法时，自动将调用该方法的对象赋值给self；
类方法：由类调用； 至少一个cls参数；执行类方法时，自动将调用该方法的类复制给cls；
静态方法：由类调用；无默认参数；
'''

'''
应用场景：如果对象中需要保存一些值，执行某功能时，需要使用对象中的值--->普通方法
         不需要任何对象中的值--->静态方法
         
'''

class Foo:
     #普通方法
     def bar(self):
         #self是对象
         print('bar')

     #静态方法
     @staticmethod
     def fun():
         print('123')


     @staticmethod
     def sta(n,m):
         print("%s--%s" % (n,m))
     #类方法
     @classmethod
     def classmd(cls):
         #cls 是类名
         print(cls)
         print('classmd')

#普通方法的调用
obj = Foo()
obj.bar()#bar

obj = Foo()
Foo.bar(obj)#bar

#静态方法的调用
Foo.fun()#123
Foo.sta('hs','yy')#hs--yy

#类方法的调用
Foo.classmd()#<class '__main__.Foo'>
             #classmd