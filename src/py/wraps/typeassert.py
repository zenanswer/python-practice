#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # if not __debug__:
        #     return func
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argment {} must be {}'.format(
                                name, bound_types[name]))
            return func(*args, **kwargs)
        return wrapper
    return decorate


#      type(x,     y, z)
@typeassert(int, str, z=int)
def spamXYZ(x, y, z=42):
    print(x, y, z)


spamXYZ(1, 'hello', 3)

try:
    spamXYZ(1, 2, 3)
except (TypeError) as e:
    print(e)


#      type(x,   z), skip y
@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)


spam(1, 'hello', 'world')
# TypeError exception here
