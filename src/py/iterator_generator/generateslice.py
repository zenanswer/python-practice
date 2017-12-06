#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import itertools


# define a generator,
# no "return" or "stop condition" in it.
def count(n):
    while True:
        yield n
        n += 1

# a daed loop here
# for x in count(10):
#     print(x)


# using itertools.islice to create a slice
# [15 -> 19]
for x in itertools.islice(count(0), 15, 20):
    print(x)
# [25 -> 29]
for x in itertools.islice(count(10), 15, 20):
    print(x)
