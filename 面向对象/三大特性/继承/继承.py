#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:18
# @Author   : 洪松
# @File     : 继承.py


'''
父类----》子类
基类----》派生类
'''

class F:

    def f1(self):
        print('F.f1')

    def f2(self):
        print('F.f2')


class S(F):

    def s1(self):
        print('S.s1')

    # def f2(self):#----重写父类中的f2,防止执行父类中的方法-----#
    #     print('S.f2')

    def f2(self):
        print('S.f2')
        super(S, self).f1()#执行父类(基类)中的f1方法
        #F.f2(self)#执行父类(基类)中的f2方法  #通过类名调用f2需要把self传给f2

obj = S()
# obj.s1()#S.s1
# obj.f2()#S.f2

obj.s1()
obj.f2()


# obj = S()
# obj.s1()# s1中的self是形参，此时代指obj
# obj.f1()#self永远指该方法的调用者