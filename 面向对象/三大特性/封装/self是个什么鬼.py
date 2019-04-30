#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:21
# @Author   : 洪松
# @File     : self是个什么鬼.py

class Bar:

    #创建类中的函数
    def foo(self,arg):
        print(self,arg)

#根据类Bar创建对象z1
z1 = Bar()#z1就是中间人
# print(z1)#<__main__.Bar object at 0x000001DFC4954FD0>
# z1.foo(111)#<__main__.Bar object at 0x000001DFC4954FD0> 111
# print('==========================')
# z2 = Bar()
# print(z2)#<__main__.Bar object at 0x000001DFC4A03390>
# z2.foo(666)#<__main__.Bar object at 0x000001DFC4A03390> 666



class Bar:
    '''self代指调用方法的对象(中间人)'''
    def foo(self,arg):
        print(self,self.name,self.age,self.gender,arg)


z = Bar()
z.name = 'hongsong'
z.age = '24'
z.gender = 'male'
z.foo(666)

z1 = Bar()
z.name = 'yangyang'
z.age = '21'
z.gender = 'famale'
z.foo(555)