# -*- coding:utf8 -*-
# @TIME     :2019/5/23 10:48
# @Author   : 洪松
# @File     : tibei_dic_insert_into_db.py
import pymysql

conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='tibet_dic')
cursor = conn.cursor()


def word_dic():
    with open('D:\全藏字快速排序\藏汉词典.txt', 'r', encoding='utf-16') as f:
        li = []
        for i in f.readlines():
            x = i.split('\t')
            li.append(x)
        for j in li:
            yield (j[0],j[1])


cursor.executemany('insert into 藏汉词典(词语, 解释) values(%s,%s)', word_dic())

conn.commit()
cursor.close()
conn.close()