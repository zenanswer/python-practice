#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import datetime


def timeonclass(cls):
    print('timeonclass')
    # save the origin __getattribute__ func
    orig_getattribute = cls.__getattribute__

    # def a new __getattribute__ func
    def new_getattribute_func(self, name):
        print(datetime.datetime.now(), 'New __getattribute__', name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = new_getattribute_func

    return cls


@timeonclass
class SomeClass:
    def dosth_1(self):
        print('SomeClass dosth_1')

    def dosth_2(self):
        print('SomeClass dosth_2')


if __name__ == '__main__':
    sl = SomeClass()
    sl.dosth_1()
    sl.dosth_2()
