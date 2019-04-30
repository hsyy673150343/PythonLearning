#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:47
# @Author   : 洪松
# @File     : 属性.py

'''Python中的属性其实是普通方法的变种'''

'''
class Test:
    def __init__(self):
        self.name = 'hs'

    def bar(self):
        print('bar')

    #用于执行obj.fun
    @property
    def fun(self):
        # print('123')
        return 1  #属性也能返回值

    #obj.fun = 123
    @fun.setter
    def fun(self, val):
        print(val)

    @fun.deleter
    def fun(self):
        print('666')

# obj = Test()

# obj.bar()#bar   #调用方法

# obj.fun#123   #调用属性

obj = Test()
ret = obj.fun
# print(ret)# 1

obj.fun = 123
# del obj.fun

'''


# '''
# 利用属性是实现分页
# '''
#
#
# class Pergination:
#
#     def __init__(self,current_page):
#         try:
#             p = int(current_page)
#         except Exception  as e:
#             p = 1
#
#         self.page = p
#     @property
#     def start(self):
#         val = (self.page - 1) * 10
#         return val
#
#     @property
#     def end(self):
#         val = self.page * 10
#         return val
#
# li = []
# for i in range(1000):
#     li.append(i)
#
#
# while True:
#     p = input('请输入要查看的页码：') #每页显示10条
#     obj = Pergination(p)
#     print(li[obj.start:obj.end])





class Foo:

     def f1(self):
         return 123

     def f2(self,val):
         print(val)

     def f3(self):
         print('del')


     per = property(fget=f1,fset=f2,fdel=f3)
     '''上面这种写法等同于'''
     # @property
     # def f1(self):
     #     return 123

     # @f2.setter
     # def f2(self,val):
     #     print(val)

     # @f3.deleter
     # def f3(self):
     #     print('del')

obj = Foo()

# ret = obj.per
# print(ret)

# obj.per = 456789

del obj.per