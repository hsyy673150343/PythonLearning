#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:02
# @Author   : 洪松
# @File     : 成员修饰符.py


# class Foo:
#     def __init__(self,name,age):
#         self.name = name    #普通字段
#         # self.age = age
#         self.__age = age    #私有字段，外部无法直接访问
#
#     def show(self):
#         return self.__age
#
#
# obj = Foo('hongsong','19')
# print(obj.name)
#
# #print(obj.__age)#私有成员，外部无法直接访问
# ret = obj.show()#可以间接访问
# print(ret)



# class Bar:
#     __v = '123'#静态字段,也能私有化
#
#     def __init__(self):
#         pass
#
#     def show(self):
#         return Bar.__v
#
#     @staticmethod
#     def stat():
#         return Bar.__v
# #print(Bar.v)#不能直接访问 #type object 'Bar' has no attribute 'v'
#
# # ret = Bar().show()
# # print(ret)
#
# ret = Bar.stat()
# print(ret)


# class Fun:
#
#     def __f1(self):#私有方法
#         return 123
#     def f2(self):
#         r = self.__f1()
#         return r
#
# # obj = Fun()
# # ret = obj.f1()
# # print(ret) #私有方法不能直接访问 #'Fun' object has no attribute 'f1'
#
# obj = Fun()
# ret = obj.f2()
# print(ret) #123



class F:
    def __init__(self):
        self.age = 15
        self.__id = 2


class S(F):
    def __init__(self,name):
        self.name = name
        self.__sex = 'male'
        super(S,self).__init__()

    def show(self):
        print(self.name)
        print(self.__sex)
        print(self.age)
        #print(self.__id) #不能访问父类里的私有字段

s = S('yy')
s.show()