#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# mattkang @ csdn
# http://blog.csdn.net/handsomekang/article/details/39895871


class Integer(object):
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__['_' + self.name] = value

    def __get__(self, instance, objtype):
        if hasattr(instance, '_' + self.name):
            return instance.__dict__['_' + self.name]
        raise NameError('No this attr [%s].' % self.name)


class Point(object):
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x):
        self.x = x


if __name__ == '__main__':
    p = Point(2)
    p.x = 9
    try:
        p.x = 9.9
    except Exception as exp:
        print('Got Excepton:' + str(exp))
    print(p.x)
    try:
        print(p.y)
    except Exception as exp:
        print('Got Excepton:' + str(exp))
