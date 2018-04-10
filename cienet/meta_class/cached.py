#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# http://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p13_using_mataclass_to_control_instance_creation.html#

import weakref


class Cached(type):
    def __init__(self, *args, **kwargs):
        self.__cache = weakref.WeakValueDictionary()
        super().__init__(*args, **kwargs)

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


# Example
class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name


if __name__ == '__main__':
    print('Try to create one Spam Guido')
    a = Spam('Guido')
    print('Try to create another Spam Guido')
    b = Spam('Guido')
    if a is b:
        print('a and b are same.')
    else:
        pass
    print('Try to create another Spam Diana')
    c = Spam('Diana')
    if a is not c:
        print('a and b are not same.')
    else:
        pass
    print('Test done.')
