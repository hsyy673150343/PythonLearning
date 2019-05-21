# -*- coding:utf8 -*-
# @TIME     :2019/5/20 20:39
# @Author   : 洪松
# @File     : 插入数据.py

import pymysql

# 创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='ssl')
# 创建游标
cursor = conn.cursor()

# 执行SQL
cursor.execute('insert into test1(name, age) values("洪松", "24")')

# r = cursor.execute('insert into test1(name, age) values("洪松", "24")')
# # 1  ---》执行SQL受影响的行数
# print(r)


# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()