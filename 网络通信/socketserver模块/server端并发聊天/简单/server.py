#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/3/15 17:17
# @Author   : 洪松
# @File     : server.py

import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print ("服务端启动...")
        while True:
            conn = self.request
            print (self.client_address)
            while True:
                client_data=conn.recv(1024)
                print (str(client_data,"utf8"))
                print ("waiting...")
                conn.sendall(client_data)
            conn.close()

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8091),MyServer)
    server.serve_forever()