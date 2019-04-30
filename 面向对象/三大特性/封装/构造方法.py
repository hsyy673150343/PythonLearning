#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 15:02
# @Author   : 洪松
# @File     : 构造方法.py

'''如果多个函数中有一些相同参数时，转换成面向对象'''


'''
构造方法
----》特殊作用：在obj = 类名()时：--->创建对象--->通过对象自动执行类中的构造方法
'''

# class Test_1:
#     def __init__(self):
#         '''
#         构造方法
#         '''
#         print('ok')
#     def fun(self):
#         print('123')
#
# s = Test_1()#ok
# print(s)#<__main__.Test_1 object at 0x00000217652741D0>
# s.fun()#123


# class Test_2:
#     def __init__(self,name,age):
#         '''构造方法'''
#         self.name = name
#         self.age = age
#     def fun(self):
#         print('123')
#
# z = Test_2('hongsong','24')
# print(z.name,z.age)#hongsong 24


'''封装'''

class Person:

    def __init__(self,name,age):
        self.n = name
        self.a = age
        self.s = 'male'

    def show(self):
        print('%s--%s--%s' % (self.n,self.a,self.s))




hs = Person('hongsong',24)
hs.show()#hongsong--24

yy = Person('yangyang',21)
yy.show()#yangyang--21


'''
综上所述，对于面向对象的封装来说，其实就是使用构造方法将内容封装到对象中，然后通过对象直接或者self间接获取被封装的内容。
'''

