#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 14:39
# @Author   : 洪松
# @File     : 特殊成员.py

'''
构造方法的执行是由创建对象触发的，即：对象 = 类名() ；
而对于 __call__ 方法的执行是由对象后加括号触发的，
即：对象() 或者 类()()
'''
# class Foo:
#     def __init__(self):
#         print('init')
#
#     def __call__(self, *args, **kwargs):
#         print('call')
#
# obj = Foo()
# #加上__call__才会执行
# obj()#init
#      #call

# class Bar:
#     def __init__(self):
#         pass
#     def __int__(self):
#         return 123
#     def __str__(self):
#         return 'yy'
#
#
# obj = Bar()
# print(obj,type(obj))  #<__main__.Bar object at 0x00000221BB834278> <class '__main__.Bar'>
#
# '''int(对象)-->会自动执行对象的__int__方法，并将返回值赋值给int(对象)'''
# i = int(obj)
# print(i)#123
#
#
# s = str(obj)
# print(s)#yy


# class Fpp:
#     def __init__(self,n,a):
#         self.name = n
#         self.age = a
#
#     def __str__(self):
#         return '%s--%s' % (self.name,self.age)
#
#
# obj = Fpp('yy','18')
# '''打印的时候会自动调用对象里的__str__方法'''
# print(obj)#相当于是print(str(obj))    #yy--18


# class Add:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __add__(self, other):
#         #self = obj_1('hs',15)
#         #other = obj_2('yy',16)
#
#         #return 123
#
#         return self.age + other.age
#     def __del__(self):
#         print('析构方法') #对象被销毁时自动执行
#
#
# obj_1 = Add('hs',15)
# obj_2 = Add('yy',16)
# '''两个对象相加时，会自动执行第一个对象的__add__方法，并且将第二个对象当作参数传递进去'''
# r = obj_1 + obj_2
# # print(r,type(r))#123 <class 'int'>
# print(r,type(r)) #31 <class 'int'>





'''__dict__ 将对象中封装的所有内容通过字典的形式返回'''


# class Dict:
#     '''
#     注释
#     '''
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __getitem__(self, item):
#         # return item + 10
#
#         # print(item,type(item))
#         '''
#         如果item是基本类型：int,str---索引获取
#         如果是slice对象的话----切片
#         '''
#         if type(item) == slice:
#             print('调用者希望内部做切片处理')
#         else:
#             print('调用者希望内部做索引处理')
#
#
#     def __setitem__(self, key, value):
#         print(key,value)
#
#
#     def __delitem__(self, key):
#         print(key)


# obj = Dict('hs','22')

# d = obj.__dict__
# print(d) #{'name': 'hs', 'age': '22'}

# ret = Dict.__dict__
# print(ret)#{'__module__': '__main__', '__doc__': '\n    注释\n    ',
#           # '__init__': <function Dict.__init__ at 0x000001DE2EE1ABF8>,
#           # '__dict__': <attribute '__dict__' of 'Dict' objects>,
#           # '__weakref__': <attribute '__weakref__' of 'Dict' objects>}


# li = Dict('yy','21')
# r = li[8] #自动执行li对象的类中的__getitem__方法，8当作参数传递给item
# print(r)
#
# li[100] = 'haha' #100 haha
#
# del li[456] #456


# lis = Dict('lili',24)
# lis[34]# 34 <class 'int'>
# lis[1:6:2]# slice(1, 6, 2) <class 'slice'>



class Iter:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __iter__(self):
        return  iter([1,2,3])

#如果类中有__iter__方法，对象---》可迭代对象
#对象.__iter__()的返回值时一个迭代器
#for循环对象如果是迭代器，那么就会不断调用next()方法去取值
#for循环对象如果是可迭代对象-->对象.__iter__()--->得到一个迭代器--->再调用next()方法

li = Iter('hs',16)


for i in li:
    '''
    1.---->执行li对象的类Iter中的__iter__方法，并获取其返回值
    2.---->循环上一步中返回的对象
    '''
    print(i)