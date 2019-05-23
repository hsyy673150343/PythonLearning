# -*- coding:utf8 -*-
# @TIME     :2019/5/23 9:58
# @Author   : 洪松
# @File     : 连表操作.py

import pymysql

conn = pymysql.connect(host='localhost', port=3306, passwd='123456',user='root',db='ssl')

cursor = conn.cursor()

cursor.execute('select *from score left join student on score.student_id=student.sid')
cursor.execute('select *from score left join course on score.course_id=course.co_id')

sql_1 = cursor.execute('select score.student_id from score inner join student on score.student_id=student.sid')
print(cursor.fetchall())
sql_2 = cursor.execute('select score.course_id from score inner join course on score.course_id=course.co_id')
print(cursor.fetchall())

conn.commit()
cursor.close()
conn.close()