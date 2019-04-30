#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 12:48
# @Author   : 洪松
# @File     : os模块.py


'''
os模块是与操作系统交互的一个接口
'''

import os


print(os.getcwd())#获取当前工作目录，即当前python脚本工作的目录路径

os.chdir(r'C:\Users')#改变当前脚本工作目录；相当于shell下cd
print(os.getcwd())

print(os.curdir)#返回当前目录: ('.')
print(os.pardir)#获取当前目录的父目录字符串名：('..')


os.makedirs('hongsong\\yangyang')#可生成多层递归目录
os.removedirs('hongsong\\yangyang')#若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推(只能删除空文件)


os.mkdir('limin')#生成单级目录；相当于shell中mkdir dirname
os.mkdir('limin\\haha')#生成单级目录；相当于shell中mkdir dirname
os.rmdir('limin\\haha')#删除单级空目录，(不会递归到上一级目录)若目录不为空则无法删除，报错；相当于shell中rmdir dirname

print(os.listdir(r'C:\Users\hongsongyangyang\PycharmProjects\老男孩python\函数'))#列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印

os.remove('limin\\haha.py')#只能删除一个文件,不能删除一个文件夹

os.rename('limin','yangyang')#os.rename("oldname","newname")  重命名文件/目录

info = os.stat('.\\yangyang')#获取文件/目录信息
print(info.st_size)#文件大小
print(info)

print(os.sep)#输出操作系统特定的路径分隔符，win下为"\ ",Linux下为"/"
print(os.linesep)#输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
print(os.pathsep)#输出用于分割文件路径的字符串 win下为;,Linux下为:
print(os.name)#输出字符串指示当前使用平台。win->'nt'; Linux->'posix'

print(os.system('dir'))#运行shell命令，直接显示
print(os.environ)#获取系统环境变量

print(os.path.abspath('./yangyang'))#返回path规范化的绝对路径
print(os.path.split(r'C:\Users\hongsongyangyang\PycharmProjects\老男孩python\模块\yangyang'))#将path分割成目录和文件名二元组返回
print(os.path.dirname(r'C:\Users\hongsongyangyang\PycharmProjects\老男孩python\模块\yangyang'))#返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.basename(r'C:\Users\hongsongyangyang\PycharmProjects\老男孩python\模块\yangyang'))#返回path最后的文件名。如果path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素

'''
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  如果path是绝对路径，返回True
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
'''

print(os.path.getatime(r'C:\Users\hongsongyangyang\PycharmProjects\老男孩python\模块\yangyang'))#返回path所指向的文件或者目录的最后存取时间
print(os.path.getmtime(r'C:\Users\hongsongyangyang\PycharmProjects\老男孩python\模块\yangyang'))#返回path所指向的文件或者目录的最后修改时间

