#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
from functools import wraps, partial


def timethis(func=None, more="default more"):
    if func is None:
        print('timethis func is None')
        return partial(timethis, more=more)

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, more, end-start, more)
        return result

    # for timethis
    return wrapper


@timethis(more="with some more")
def countdown(n):
    print('countdown')
    while n > 0:
        n -= 1


@timethis
def countdown2(n):
    print('countdown2')
    while n > 0:
        n -= 1


countdown(100000)

countdown2(100000)
