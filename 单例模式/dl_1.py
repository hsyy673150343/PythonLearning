#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 16:28
# @Author   : 洪松
# @File     : dl_1.py

import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        import time

        self.write(str(time.time()))

application = tornado.web.Application([
    (r'/index',MainHandler),])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()