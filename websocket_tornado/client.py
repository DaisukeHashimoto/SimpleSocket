#!/usr/bin/env python
# -*- coding: utf_8 -*-

import websocket
import thread
import time

URL = "ws://localhost:8888/websocket"


def on_message(ws, message):
    print message


def on_error(ws, error):
    print error


def on_close(ws):
    print "### closed ###"


def on_open(ws):
    def run(*args):
        for i in range(30000):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print "thread terminating..."
    thread.start_new_thread(run, ())


def main():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(URL,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    ws.run_forever()


if __name__ == '__main__':
    main()
