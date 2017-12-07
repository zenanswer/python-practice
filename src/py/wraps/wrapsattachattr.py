#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
from functools import wraps, partial


def timethisandmore(more="default more here"):
    print('timethisandmore in')

    # 1st time, invoked by "@attach_wrapper(wrapper)", so the func is None
    # 2nd time, invoked by "attach_wrapper(obj, func)", the real wrapper.
    def attach_wrapper(obj, func=None):
        print(type(obj), obj.__name__, type(func))
        if func is None:
            # https://docs.python.org/2/library/functools.html#functools.partial
            # http://www.wklken.me/posts/2013/08/18/python-extra-functools.html#functoolspartial
            # return a partial function:
            # function(func) = attach_wrapper(obj, func)
            return partial(attach_wrapper, obj)
        print(func.__name__)
        # https://docs.python.org/3/library/functions.html#setattr
        # obj."func.__name__" = func
        setattr(obj, func.__name__, func)
        # return func  # here is not need to return func

    def timethis(func):
        print('timethis in')
        '''
        Decorator for execution time
        '''
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(func.__name__, more, end-start)
            return result  # for wrapper(*args, **kwargs)

        print('call attach_wrappe')

        @attach_wrapper(wrapper)
        def setmore(newmore):
            nonlocal more
            more = newmore

        print('return wrapper')
        # for timethis(func)
        return wrapper

    # for timethisandmore(more="")
    return timethis


print("Add @timethisandmore")


@timethisandmore("customized more here")
def countdown(n: int):  # countdown.__annotations__
    '''
    A count down function
    '''
    while n > 0:
        n -= 1


countdown(10)

countdown.setmore("re-set through setmore")

countdown(10)
