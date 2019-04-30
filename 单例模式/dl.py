#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 15:54
# @Author   : 洪松
# @File     : dl.py

'''单例-----永远使用同一个实例(对象)'''


class Foo:
    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return  cls.__v


obj_1 = Foo.get_instance()
print(obj_1)
obj_2 = Foo.get_instance()
print(obj_2)
obj_3 = Foo.get_instance()
print(obj_3)
'''
<__main__.Foo object at 0x000001AF01D6B908>
<__main__.Foo object at 0x000001AF01D6B908>
<__main__.Foo object at 0x000001AF01D6B908>
'''