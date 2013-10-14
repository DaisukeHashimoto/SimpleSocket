#!/usr/bin/env python
# -*- coding: utf_8 -*-

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


def main():
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    first_data = tcpCliSock.recv(BUFSIZ)
    print 'first_data:', first_data

    while True:
        data = raw_input('> ')
        if not data:
            break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print data

    tcpCliSock.close()


if __name__ == '__main__':
    main()
