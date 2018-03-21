#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class MyClass:
    var_in_MyClass = 0

    def __init__(self):
        self.var_in_MyObj = 1


def show_info(sth):
    print('**** %s ****\n%s\n' % (sth, repr(eval(sth))))


if __name__ == '__main__':

    show_info('type(MyClass)')
    show_info('type(MyClass).__dict__')
    mc = MyClass()
    show_info('MyClass')
    show_info('MyClass.__dict__')
    show_info('type(mc)')
    show_info('type(mc).__dict__')
    show_info('mc')
    show_info('mc.__dict__')
    show_info('show_info')
    show_info('type(__name__)')
