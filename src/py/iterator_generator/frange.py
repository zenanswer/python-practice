#!/usr/bin/python
# -*- coding: UTF-8 -*-


def frange(start, stop, increment):
    x = start
    print('frange start from:%d' % x)
    while x < stop:
        # 1. the value of x will be return,
        # 2. this func will be paused here,
        # 3. and x's value will be keep until another "next" invoked
        # print('frange A:%d' % x)
        yield x
        x += increment
        # print('frange B:%d' % x)
    print('frange done:%d' % x)


if __name__ == '__main__':

    for n in frange(1, 2, 0.3):
        print(n)

    print list(frange(1, 2, 0.3))

    fr = frange(1, 2, 0.3)
    try:
        print next(fr)
        print next(fr)
        print next(fr)
        print next(fr)
        # will throw a StopIteration exception
        print next(fr)
    except StopIteration:
        print('Got StopIteration')
