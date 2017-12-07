#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
from functools import wraps


def external(externalparm='externalparm'):
    print('external layer:', externalparm)

    def interior(func):
        print('interior layer:', type(func), func.__name__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print('wrapper:', func.__name__, end-start, externalparm)
            return result

        print('interior layer exit')
        return wrapper

    print('external layer exit')
    return interior


print("Definition of printsth")


@external("external's parm")
def printsth(something: str):
    time.sleep(0.050)
    print(something)


print("Run printsth")

printsth('I want to print sth.')
# Out put:
# Definition of printsth
# external layer: external's parm
# external layer exit
# interior layer: <class 'function'> printsth
# interior layer exit
# Run printsth
# I want to print sth.
# wrapper: printsth 0.05035686492919922 external's parm
