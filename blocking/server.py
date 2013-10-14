#!/usr/bin/env python
# -*- coding: utf_8 -*-

from socket import *
from time import ctime

HOST = '127.0.0.1'   # localhost
PORT = 21567         # choose a random port number
BUFSIZ = 1024        # set buffer size to 1K
ADDR = (HOST, PORT)

MAX_CONNECTION = 5


def main():
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(MAX_CONNECTION)

    while True:
        print 'waiting for connection...'
        tcpCliSock, addr = tcpSerSock.accept()
        print '...connected from:', addr
        tcpCliSock.send('WELCOME!!!')

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            tcpCliSock.send('[%s] %s' % (ctime(), data))

        tcpCliSock.close()

    tcpSerSock.close()  # never executed


if __name__ == '__main__':
    main()
