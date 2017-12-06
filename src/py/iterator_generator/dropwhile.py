#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import itertools

print('itertools.dropwhile:')
# 6, 4, 1
for x in itertools.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]):
    print(x)


def g(n):
    while n < 20:
        yield n
        n += 1


print('generator::')
# print out 15 -> 19
for x in g(15):
    print(x)

print('itertools.dropwhile and generator ==17:')
# 15 -> 19
for x in itertools.dropwhile(lambda x: x == 17, g(15)):
    print(x)

print('itertools.dropwhile and generator <17:')
# 17 -> 19
for x in itertools.dropwhile(lambda x: x < 17, g(15)):
    print(x)
