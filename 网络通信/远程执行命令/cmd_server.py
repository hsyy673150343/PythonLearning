#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/13 18:45
# @Author   : 洪松
# @File     : cmd_server.py


import socket
import subprocess

sk = socket.socket()#创建socket对象

address = ('127.0.0.1',8000)#IP地址和端口

sk.bind(address)#绑定IP地址和端口--->告诉client端，server端开的服务在哪儿。

sk.listen(3)#决定client端可以排3个人等待
print('waiting....')

while True:
    conn, addr = sk.accept()  # 阻塞，等待client端来连接
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
        except Exception:
            break
        if not data:
            break
        print('......', str(data, 'utf8'))

        obj = subprocess.Popen(str(data,'utf8'),shell=True,stdout=subprocess.PIPE)
        cmd_result = obj.stdout.read()#调用的Windows下的shell命令，windows下编码默认为gbk

        result_len = bytes(str(len(cmd_result)),'utf-8')#int不能直接转成byte类型,但是str可以转成byte类型
        print('>>>>',result_len)
        '''两次连续发可能会出现粘包现象'''
        conn.sendall(result_len)
        conn.recv(1024)#防止粘包现象
        conn.send(cmd_result)


sk.close()