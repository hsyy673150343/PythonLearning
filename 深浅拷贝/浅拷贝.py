#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 17:14
# @Author   : 洪松
# @File     : 浅拷贝.py
'''

在使用浅拷贝的时候，发现引用的id都是相同的，
但是字符串的id却发生了变化，是因为在python中，
字符串是不可变的，从而在每次进行修改的时候，
都是新建一个对象，从而引用发生了变化。

在不可变类型中，数字和字符串都是不可变类型，
从而在每次修改的时候，都是新创建一个对象。

'''


# s1 = [1,'hongsong','yangyang']
# s2 = s1.copy()
# print(s2)
#
# s2[0] = 2
# print(s1)
# print(s2)
#
#
# s3 = [[1,2],'hongsong','yangyang']
# s4 = s3.copy()
# print(s4)
#
# s4[1] = 'linux'
# print(s3)
# print(s4)
#
# s4[0][1] = 3
# print(s4)
# print(s3)



a = [[1,2],3,4]
b = a.copy()
b[1] = 'hongsong'
print(a)
print(b)

b[0][0] = 8
print(a)
print(b)