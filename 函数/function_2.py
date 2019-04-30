#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:35
# @Author   : 洪松
# @File     : function_2.py

'''
函数的参数
'''

'''
必需的参数：必需参数须以正确的顺序传入函数。
调用时的数量必须和声明时的一样。
'''

def print_info(name,age,sex='male'):#sex就是默认参数(注意：(定长参数)默认参数要跟在非默认参数后面，否则会报错)
    print('Name: %s' %name)
    print('Age: %d' %age)
    print('Sex: %s' %sex)

print_info('hongsong',24)#必需参数
print_info(age=24, name='hongsong')#关键字参数
print_info('yangyang',21,'female')



def add(*args):#一个星号*args不定长参数(不命名参数)---》存入元组里
    print(args)
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(1,2,3,3)


'''
不定长参数的位置：
*args不命名参数放左边,**kwargs命名参数放右边

'''

# def print_info(*args,**kwargs):#两个星号**kwargs命名参数--》键值对---》存入字典里
#     print(args)
#     for i in kwargs:
#         print('%s : %s' % (i,kwargs[i]))
# print_info('hongsong',24,'male',job='IT',hobby='reading')


'''
参数位置：非默认参数-->默认参数-->不命名参数-->命名参数
'''
def print_info(sex='male',*args,**kwargs):#(不定长参数)默认参数可以放在非默认参数前边，但不能放在非默认参数后边
    print('Sex: %s' %sex)
    print(args)
    for i in kwargs:
        print('%s : %s' % (i,kwargs[i]))
print_info('hongsong',24,'male',job='IT',hobby='reading')


'''
函数返回值(return):结束函数，返回一个对象。
函数里如果没有return，会默认返回一个None
如果return多个对象，那么python会帮我们把多个对象封装成一个元组返回。
'''


