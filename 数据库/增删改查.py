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

# 增加数据
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


# def word_dic():
#     with open('D:\全藏字快速排序\藏汉词典.txt', 'r', encoding='utf-16') as f:
#         li = []
#         for i in f.readlines():
#             x = i.split('\t')
#             li.append(x)
#         for j in li:
#             yield (j[0],j[1])
#
#
# cursor.executemany('insert into 藏汉词典(音节, 解释) values(%s,%s)', word_dic())

# 修改数据
# cursor.execute('update test1 set name = %s where age = %s', ('王明', 22))

# 删除数据
# cursor.execute('delete from test1 where age = %s', (21,))

# 查询数据----可以不用commit()
# row = cursor.execute('select *from test1')
# print(row)

# result = cursor.fetchall()
# print(result)

# result = cursor.fetchone()
# print(result)

# result = cursor.fetchmany(2)
# print(result)

# result = cursor.fetchone()
# print(result)
# result = cursor.fetchone()
# print(result)
# result = cursor.fetchone()
# print(result)

# result = cursor.fetchone()
# print(result)
# result = cursor.fetchone()
# print(result)
# cursor.scroll(0,mode='absolute') # 相对绝对位置移动
# result = cursor.fetchone()
# print(result)


# result = cursor.fetchone()
# print(result)
# result = cursor.fetchone()
# print(result)
# cursor.scroll(0,mode='relative')  # 相对当前位置移动 -1, 0, 1.....
# result = cursor.fetchone()
# print(result)

cursor.execute('select *from test1 where name=%s',('洪松',))
# print(cursor.fetchall())#(('洪松', 24),)
print(cursor.fetchone())#('洪松', 24)

conn.commit()
cursor.close()
conn.close()

