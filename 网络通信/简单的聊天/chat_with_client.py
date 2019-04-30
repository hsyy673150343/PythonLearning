#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/12 20:06
# @Author   : 洪松
# @File     : chat_with_client.py

import socket

sk = socket.socket()#创建socket对象

address = ('127.0.0.1',8000)

sk.connect(address)#连接IP地址和端口

while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp,'utf8'))#发送的byte类型

    data = sk.recv(1024)
    print(str(data,'utf8'))


sk.close()
print(sk)