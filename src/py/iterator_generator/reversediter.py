#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # for "reversed()" function
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


print('CountDown:')
# print 20 -> 1
for cd in CountDown(20):
    print(cd)

print('reversed CountDown:')
# print 1 -> 20
for rcd in reversed(CountDown(20)):
    print(rcd)
