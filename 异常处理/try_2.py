#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:56
# @Author   : 洪松
# @File     : try_2.py


'''主动触发异常'''

try:
    raise Exception('错误了。。。')
except Exception as e:
    print(e)


def db():
    #return True
    return False

def index():
    try:
        result = db()
        if not result:
            raise Exception('数据库处理错误')
    except Exception as e:
        str_err = str(e)
        print(str_err)