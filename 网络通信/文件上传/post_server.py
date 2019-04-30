#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/14 13:34
# @Author   : 洪松
# @File     : post_server.py


import socket
import os

sk = socket.socket()#创建socket对象

address = ('127.0.0.1',8000)#IP地址和端口

sk.bind(address)#绑定IP地址和端口--->告诉client端，server端开的服务在哪儿。

sk.listen(3)#决定client端可以排3个人等待
print('waiting....')
'''
__file__  是用来获得模块所在的路径的，这得到的是一个相对路径
os.path.abspath()--->把相对路径转换为绝对路径 
os.path.dirname()--->测试脚本所在的位置
'''
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)#C:\Users\hongsongyangyang\PycharmProjects\OldBoyPython\网络通信\文件上传

while True:
    conn, addr = sk.accept()  # 阻塞，等待client端来连接
    while True:
        '''接收post命令、file_name、file_size'''
        data = conn.recv(1024)
        cmd,file_name,file_size = str(data,'utf-8').split('|')
        path = os.path.join(BASE_DIR,'hongsong',file_name)
        file_size = int(file_size)

        with open(path,'ab') as f:
            has_recv = 0
            while has_recv != file_size:
                data = conn.recv(1024)
                f.write(data)
                has_recv += len(data)


sk.close()