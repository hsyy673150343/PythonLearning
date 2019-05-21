# -*- coding:utf8 -*-
# @TIME     :2019/5/21 21:04
# @Author   : 洪松
# @File     : 增删改查.py

import pymysql

conn = pymysql.connect(host='localhost', port=3306, passwd='123456', user='root',db='ssl')
cursor = conn.cursor()

# 字符串拼接sql语句, 可以执行 ----禁止这样使用
# inp_name = input('请输入姓名：')
# inp_age = input('请输入年龄：')
# sql = 'insert into test1(name, age) values("%s", "%s")'
# sql_fina = sql % (inp_name, inp_age)
# cursor.execute(sql_fina)

# 参数传递----必须使用这种参数传入的方式
# inp_name = input('请输入姓名：')
# inp_age = input('请输入年龄：')
# cursor.execute('insert into test1(name, age) values(%s,%s)', (inp_name, inp_age))

# inp = [
#     ('李四', 22),
#     ('张三', 34),
# ]
#
# cursor.executemany('insert into test1(name, age) values(%s,%s)', inp)


def word_dic():
    with open('D:\全藏字快速排序\藏汉词典.txt', 'r', encoding='utf-16') as f:
        li = []
        for i in f.readlines():
            x = i.split('\t')
            li.append(x)
        for j in li:
            yield (j[0],j[1])


cursor.executemany('insert into 藏汉词典(音节, 解释) values(%s,%s)', word_dic())

conn.commit()
cursor.close()
conn.close()
