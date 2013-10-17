#!/usr/bin/env python
# -*- coding: utf_8 -*-

import tornado.ioloop
import tornado.web
import tornado.websocket

PORT = 8888


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print "WebSocket closed"


application = tornado.web.Application([
    (r"/websocket", EchoWebSocket),
])


def main():
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
