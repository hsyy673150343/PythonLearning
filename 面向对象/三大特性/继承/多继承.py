#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 17:19
# @Author   : 洪松
# @File     : 多继承.py
'''
python中支持多继承：
---》左侧优先
---》一条道走到黑
---》有同一个根时，根最后执行
'''


# class Base:
#     def test_before(self):
#         print('Base.test_before')
#
# class F0(Base):
#     def a1(self):
#         print('F0.test_before')
#
#
# class F1(F0):
#     def a1(self):
#         print('F1.test_before')
#
# class F2(Base):
#     def a1(self):
#         print('F2.test_before')
#
#
# class S(F1,F2):
#     pass
#
# obj = S()
# obj.test_before()#Base.test_before


class BaseReuqest:

    def __init__(self):
        print('BaseReuqest.init')

class RequestHandler(BaseReuqest):

    def __init__(self):
        print('RequestHandler.init')
        #BaseReuqest.__init__(self)#执行父类中init()方法
        #super(RequestHandler,self).__init__()##执行父类中init()方法

    def serve_forever(self):
        print('RequestHandler.serve_forever')
        self.process_request()

    def process_request(self):
        print('RequestHandler.process_request')

class Minx:
    def process_request(self):
        print('minx.process_request')


class Son(Minx,RequestHandler):
    pass


obj = Son()
obj.serve_forever()#RequestHandler.serve_forever
                   #minx.process_request


# obj = Son()#RequestHandler.init

'''
试着找一找代码执行流程流程
'''
# import socketserver
# obj = socketserver.ThreadingTCPServer()
# obj.serve_forever()