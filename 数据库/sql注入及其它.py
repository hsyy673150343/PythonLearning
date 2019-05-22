# -*- coding:utf8 -*-
# @TIME     :2019/5/22 20:39
# @Author   : 洪松
# @File     : sql注入及其它.py

import pymysql

conn = pymysql.connect(host='localhost', port=3306, passwd='123456', user='root',db='ssl')
cursor = conn.cursor()

# cursor.execute('select username,password from userinfo where username=%s and password=%s', ('yangyang', 456))
# result = cursor.fetchone()
# print(result)

# sql 注入
# s = 'select username,password from userinfo where username="%s" and password="%s"'
# sql = s % ('hongsong " -- ', 1234)
# cursor.execute(sql)
# result = cursor.fetchone()
# print(result)

# cursor.execute('select *from userinfo')
# print(cursor.fetchall()) #((1, 'hongsong', 123), (2, 'yangyang', 456))

# 关于默认获取的数据是元祖类型，如果想要或者字典类型的数据，即：
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# cursor.execute('select *from userinfo')
# print(cursor.fetchall())

# 获取新创建数据自增ID
cursor.execute('insert into userinfo(username, password) values (%s,%s)', ('李四', 789))
nid = cursor.lastrowid
print(nid)# 最后一条

conn.commit()
cursor.close()
conn.close()
