#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import functools


class LazyConnection:
    def __init__(
            self, address, family=socket.AF_INET, conntype=socket.SOCK_STREAM):
        self.address = address
        self.family = family
        self.conntype = conntype
        self.socket = None

    def __enter__(self):
        print('LazyConnection __enter__')
        if self.socket is not None:
            raise RuntimeError('Already connected.')
        self.socket = socket.socket(self.family, self.conntype)
        self.socket.connect(self.address)
        return self.socket

    def __exit__(self, exc_ty, exc_val, tb):
        print('LazyConnection __exit__')
        if self.socket is not None:
            self.socket.close()
            self.socket = None


if __name__ == '__main__':
    conn = LazyConnection(address=('www.python.org', 80))
    with conn as c:
        c.send(b'GET /index.html HTTP/1.0\r\n')
        c.send(b'Host: www.python.org\r\n')
        c.send(b'\r\n')
        # iter return an iterator object
        # (https://docs.python.org/3/library/functions.html#iter)
        # functools.partial return a new recv func = c.recv(8192)
        resp = b''.join(iter(functools.partial(c.recv, 8192), b''))
        print(resp)
