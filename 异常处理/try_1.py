#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:28
# @Author   : 洪松
# @File     : try_1.py

# while True:
#     try:
#         #代码块，逻辑
#         inp = input('请输入序号')
#         i = int(inp)
#     except Exception as e:
#         Exception可以捕获所有异常
#         #e是Exception对象，对象中封装了错误信息
#         #上述代码块如果出错，自动执行当前块的内容
#         print(e)
#         i = 1
#
#     print(i)

'''
AttributeError 试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界,比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的
'''

try:
    li = [11,22]
    # li[999]
except IndexError as e:
    print(e)
else:
    print('haha')
finally:
    print('....')