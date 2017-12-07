#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
from functools import wraps


def timethisandmore(more="here is more info."):
    def timethis(func):
        '''
        Decorator for execution time
        '''
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(func.__name__, more, end-start)
            return result

        # for timethis
        return wrapper
    # for timethisandmore
    return timethis


@timethisandmore("time cost:")
def countdown(n: int):  # countdown.__annotations__
    '''
    A count down function
    '''
    while n > 0:
        n -= 1


countdown(100000)
# countdown 0.0066568851470947266

countdown(1000000)
# countdown 0.0733339786529541

print(countdown.__name__)
# countdown

print(countdown.__doc__)
# A count down function

print(countdown.__annotations__)  # def countdown(n:int):
# {'n': <class 'int'>}
