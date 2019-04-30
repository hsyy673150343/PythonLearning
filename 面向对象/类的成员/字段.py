#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 13:54
# @Author   : 洪松
# @File     : 字段.py
'''
字段包括：普通字段和静态字段，他们在定义和使用中有所区别，而最本质的区别是内存中保存的位置不同，

普通字段属于对象，保存在对象中，执行只能通过对象访问
静态字段属于类，保存在类中，执行可以通过对象访问，也可以通过类访问

'''

# class Foo:
#
#     def __init__(self,name):
#         #普通字段--->属于对象
#         self.name = name
#
#     #普通方法
#     def show(self):
#         print(self.name)
#
# obj = Foo('hs')
# obj.show()


class Province:
    #静态字段---->属于类
    country = '中国'

    def __init__(self,name):
        #普通字段
        self.name = name

#直接访问普通字段
henan = Province('河南')
print(henan.name)#河南

tianjin = Province('天津')
print(tianjin.name)#天津

obj = Province('四川')
print(obj.country,obj.name)#中国 四川

#直接访问静态字段
print(Province.country)