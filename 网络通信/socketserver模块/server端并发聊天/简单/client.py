#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/15 17:17
# @Author   : 洪松
# @File     : client.py
import socket

ip_port = ('127.0.0.1',8091)
sk = socket.socket()
sk.connect(ip_port)
print ("客户端启动：")
while True:
    inp = input('>>>')
    sk.sendall(bytes(inp,"utf8"))
    if inp == 'exit':
        break
    server_response=sk.recv(1024)
    print (str(server_response,"utf8"))
sk.close()