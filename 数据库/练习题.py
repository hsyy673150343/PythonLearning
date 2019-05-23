# -*- coding:utf8 -*-
# @TIME     :2019/5/23 11:25
# @Author   : 洪松
# @File     : 练习题.py

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='123456',db='sql_example')
cursor = conn.cursor(pymysql.cursors.DictCursor)

# 题目一---查询平均成绩大于60分的同学的学号和平均成绩(思路:根据学生分组，使用avg获取平均值，通过having对avg进行筛选)
cursor.execute('select student_id, avg(num) from score group by student_id having avg(num)>60')
print(cursor.fetchall())
# ---查询平均成绩大于60分的同学的(姓名)、学号和平均成绩
cursor.execute('SELECT student_id,avg(num),sname FROM score\
                LEFT JOIN student on score.student_id = student.sid GROUP BY student_id HAVING avg(num)>60')
print(cursor.fetchall())

# 另解一：
cursor.execute('SELECT * FROM(SELECT student_id,avg(num) FROM score GROUP BY student_id HAVING avg(num)>60) as T \
                LEFT JOIN student on T.student_id=student.sid')
print(cursor.fetchall())

# 另解二：
cursor.execute('SELECT T.student_id,T.a,student.sname FROM\
                (SELECT student_id,avg(num) as a FROM score GROUP BY student_id HAVING avg(num)>60) as T\
                 LEFT JOIN student on T.student_id=student.sid')
print(cursor.fetchall())

# 题目二：查询所有同学的学号、姓名、选课数、总成绩；
cursor.execute('SELECT score.sid,student.sname,COUNT(score.student_id),SUM(score.num) FROM score \
                LEFT JOIN student on score.student_id=student.sid GROUP BY student_id')
print(cursor.fetchall())

# 题目三：查询姓“李”的老师的个数

# 查询姓“李”的老师的个数
cursor.execute('SELECT *FROM teacher WHERE tname LIKE "李%"')
print(cursor.fetchall())
# 查询姓“李”的老师的个数
# cursor.execute('SELECT COUNT(tid) FROM teacher WHERE tname LIKE "李%"')
cursor.execute('SELECT COUNT(tid) FROM(SELECT *FROM teacher WHERE tname LIKE "李%") as V')
print(cursor.fetchall())

# 题目四：查询没学过“叶平”老师课的同学的学号、姓名；(思路：先查到“李平老师”老师教的所有课ID,获取选过课的所有学生ID,学生表中筛选)
cursor.execute(' select * from student where sid not in \
              (select DISTINCT student_id from score where score.course_id in \
              (select cid from course left join teacher on course.teacher_id = teacher.tid where tname = "李平老师"))')
print(cursor.fetchall())

# 题目五：查询学过“1”并且也学过编号“2”课程的同学的学号、姓名；(思路：先查到既选择1又选择2课程的所有同学,根据学生进行分组，如果学生数量等于2表示，两门均已选择)
cursor.execute('SELECT B.student_id, sname FROM(SELECT student_id,course_id FROM score WHERE course_id=1 or course_id=2) as B \
                LEFT JOIN student on B.student_id=student.sid\
                GROUP BY B.student_id HAVING COUNT(student_id)>1')
print(cursor.fetchall())

# 题目六：查询学过“叶平”老师所教的所有课的同学的学号、姓名
cursor.execute('SELECT student_id,sname FROM(SELECT student_id FROM score WHERE \
                course_id IN (SELECT cid FROM course LEFT JOIN teacher \
                on course.teacher_id= teacher.tid WHERE teacher.tname="李平老师") GROUP BY student_id ) as A\
                 LEFT JOIN student on A.student_id=student.sid')
print(cursor.fetchall())
# 题目七：查询有课程成绩小于60分的同学的学号、姓名
# cursor.execute('SELECT student_id,sname FROM(SELECT student_id FROM score WHERE num<60 GROUP BY student_id) \
#                 as A LEFT JOIN student on A.student_id=student.sid')
#  DISTINCT 去重
cursor.execute('SELECT sid,sname FROM student where sid in (SELECT DISTINCT student_id FROM score WHERE num<60)')
print(cursor.fetchall())

# 题目八：查询没有学全所有课的同学的学号、姓名；(思路：在分数表中根据学生进行分组，获取每一个学生选课数量,如果数量 == 总课程数量，表示已经选择了所有课程)
cursor.execute('SELECT student_id,sname FROM(SELECT student_id, COUNT(student_id) FROM score GROUP BY \
                student_id HAVING COUNT(student_id) < (SELECT COUNT(course.cid) FROM course)) as A \
                LEFT JOIN student on A.student_id=student.sid')
print(cursor.fetchall())

# 题目九：查询至少有一门课与学号为“1”的同学所学相同的同学的学号和姓名；
cursor.execute('SELECT student_id,sname FROM(SELECT student_id FROM score WHERE student_id!=1 AND course_id IN\
                (SELECT course_id FROM score WHERE student_id=1)GROUP BY student_id) as A \
                LEFT JOIN student on A.student_id=student.sid')
print(cursor.fetchall())

# 题目十：查询至少学过学号为“1”同学所有课的其他同学学号和姓名
cursor.execute('SELECT student_id, sname FROM(SELECT student_id, COUNT(student_id) FROM score WHERE course_id IN(SELECT course_id FROM score WHERE student_id=1) GROUP BY student_id\
                HAVING COUNT(student_id) = (SELECT COUNT(student_id) FROM score WHERE student_id=1)) as A \
                LEFT JOIN student on A.student_id=student.sid')
print(cursor.fetchall())


conn.commit()
cursor.close()
conn.close()