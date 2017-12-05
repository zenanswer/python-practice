#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 1. yield can return a variate or nothing(just hang up)
# 2. Generators.send() method can send a variate to the yield
# 3. Generators.send(None) = next(Generators)


def g():
    start = 0
    while True:
        # 1. yield is a two-way pip
        # 2. return "start", and wait
        # 3. "inc" will be assigned,
        # after send(XXX) or next() be called from outside
        inc = yield start
        print('inc:%d' % inc)
        start += inc
        print('start:%d' % start)
        if start > 10:
            print('End')
            return


print('== Test g1 ==')

myg = g()

try:
    for x in myg:
        print(x)
        # an exception will be risen, because of inc will be a None
except TypeError as e:
    print(e)

print('== Test g2 ==')

myg2 = g()
# just call "next" at the beginning,
# if not, you will got a error:
# TypeError: can't send non-None value to a just-started generator
print(next(myg2))

print(myg2.send(1))
print(myg2.send(2))
print(myg2.send(3))
print(myg2.send(4))
try:
    print(myg2.send(5))
except StopIteration:
    print('Got StopIteration')
