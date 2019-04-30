#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/12 20:04
# @Author   : 洪松
# @File     : chat_with_server.py


import socket

sk = socket.socket()#创建socket对象

address = ('127.0.0.1',8000)#IP地址和端口

sk.bind(address)#绑定IP地址和端口--->告诉client端，server端开的服务在哪儿。

sk.listen(3)#决定client端可以排3个人等待
print('waiting....')

'''conn,addr= sk.accept()#阻塞，等待client端来连接
while True:
    data = conn.recv(1024)
    print('......','\n',str(data,'utf-8'))
    if not data:
        conn,addr = sk.accept()
        print(addr)
        continue

    inp = input('>>>')
    conn.send(bytes(inp,'utf-8'))#发送的byte类型
    
conn.close()
sk.close()'''

while True:
    conn, addr = sk.accept()  # 阻塞，等待client端来连接
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
        except Exception:
            break
        print('......',str(data,'utf8'))
        if not data:
            break
        inp = input('>>>')
        conn.send(bytes(inp,'utf8'))


sk.close()


