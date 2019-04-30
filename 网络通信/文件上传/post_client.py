#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/14 13:34
# @Author   : 洪松
# @File     : post_client.py

import socket
import os

sk = socket.socket()#创建socket对象

address = ('127.0.0.1',8000)

sk.connect(address)#连接IP地址和端口

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


while True:
    inp = input('>>>').strip()

    cmd,path = inp.split('|')

    path = os.path.join(BASE_DIR,path)
    print(path)#C:\Users\hongsongyangyang\PycharmProjects\OldBoyPython\网络通信\文件上传\1.png

    file_name = os.path.basename(path)#获取文件名
    print(file_name)#1.png

    file_size = os.stat(path).st_size#获取文件大小
    print(file_size)

    file_info = 'post|%s|%s' % (file_name,file_size)
    print(file_info)

    '''发送post命令、file_name、file_size'''
    sk.sendall(bytes(file_info,'utf-8'))

    with open(path,'rb') as f:
        has_sent = 0
        while has_sent != file_size:
            data = f.read(1024)
            sk.sendall(data)
            has_sent += len(data)
    print('上传成功')

sk.close()