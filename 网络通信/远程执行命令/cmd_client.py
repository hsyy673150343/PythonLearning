#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/13 18:45
# @Author   : 洪松
# @File     : cmd_client.py


import socket

sk = socket.socket()#创建socket对象

address = ('127.0.0.1',8000)

sk.connect(address)#连接IP地址和端口

while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp,'utf8'))#发送的byte类型

    result_len = int(str(sk.recv(1024),'utf-8'))
    print(result_len)

    sk.sendall('ok')#防止粘包现象

    data = bytes()#初始化data，因为data是byte类型所以用这种方式初始化
    while len(data) != result_len:#两者不相等，说明还没接收完
        recv = sk.recv(1024)
        data += recv

    print(str(data,'gbk'))#所以这里以'gbk'的形式解码

sk.close()
