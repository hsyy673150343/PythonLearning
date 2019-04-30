#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 17:54
# @Author   : 洪松
# @File     : client.py

'''
client下的方法：
connect()


recv()
send()
sendall()
close()
'''

'''*****发*****'''

'''import socket

sk = socket.socket()#创建socket对象

address = ('127.0.0.1',8000)

sk.connect(address)#连接IP地址和端口

data = sk.send(bytes('haha','utf8'))

sk.close()
print(sk)'''#<socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>


'''*****收*****'''


import socket

sk = socket.socket()#创建socket对象

address = ('127.0.0.1',8000)

sk.connect(address)#连接IP地址和端口

data = sk.recv(1024)#阻塞
print(str(data,'utf8'))

sk.close()
print(sk)