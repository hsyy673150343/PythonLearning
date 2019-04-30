#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 17:51
# @Author   : 洪松
# @File     : server.py


'''
server下的方法：
bind()
listen()
accept()

recv()
send()
sendall()

close()

服务器端和客户端的sk不一样
'''

'''*****一收一发的原则*****'''



'''
SOCK_STREAM:TCP
SOCK_DGRAM:UDP


family = AF_INET---服务器之间的通信
family = AF_UNIX---Unix不同进程间的通信
'''
import socket


'''****收*****'''

'''sk = socket.socket()#创建socket对象

address = ('127.0.0.1',8000)#IP地址和端口

sk.bind(address)#绑定IP地址和端口--->告诉client端，server端开的服务在哪儿。

sk.listen(3)#决定client端可以排几个人
print('waiting....')

conn,addr= sk.accept()#阻塞，等待client端来连接

data = conn.recv(1024)
print(data)

conn.close()
sk.close()'''

'''*****发*****'''
sk = socket.socket()#创建socket对象

address = ('127.0.0.1',8000)#IP地址和端口

sk.bind(address)#绑定IP地址和端口--->告诉client端，server端开的服务在哪儿。

sk.listen(3)#决定client端可以排几个人
print('waiting....')

conn,addr= sk.accept()#阻塞，等待client端来连接

inp = input('>>>')
conn.send(bytes(inp,'utf-8'))#发送的byte类型

conn.close()#结束此次通话
sk.close()
