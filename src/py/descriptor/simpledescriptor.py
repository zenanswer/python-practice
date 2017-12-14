#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Excepted an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')  # class attribute
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
