#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 11:27
# @Author   : 洪松
# @File     : 集合.py

'''
集合的创建----无序、不重复
分为：
可变集合(set)中的元素是可哈希的，set集合整体是不可哈希的(即可变的)。
集合对象一定是可哈希的值(即不可变的)，集合成员可以做字典的键,因为字典的键必须是不可变的。

[TypeError: unhashable type: 'list'
s4中有list[1,2],list是不可哈希的
s4 = [[1,2],'test_before','b']
s5 = set(s4)
print(s5)
TypeError: unhashable type: 'list']

不可变集合(frozenset)
'''

s = set('hongsong')
print(s)

s1 = {'hongsong','yangyang','hongsong'}
s2 = set(s1)
print(s2,type(s2))

s3 = list(s2)
print(s3,type(s3))

'''
访问集合：只能通过循环遍历或者使用in，
not in来访问或判断集合元素
'''

