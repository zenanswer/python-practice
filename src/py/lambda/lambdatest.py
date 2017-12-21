#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import functools

# https://www.cnblogs.com/evening/archive/2012/03/29/2423554.html


if __name__ == '__main__':
    g = lambda x:x+1
    # def g(x):
    #     return x+1
    print(g(1))  # 2
    print(g(2))  # 3

    # define a function, and return a lambda
    def make_incrementor(n):
        print('make_incrementor:', n)
        return lambda x: x + n

    pluse2 = make_incrementor(2)
    pluse3 = make_incrementor(3)

    print(pluse2(5))  # n=2, x=5, return 7
    print(pluse3(5))  # n=3, x=5, return 8

    print(make_incrementor(1)(99))  # n=1, x=99, return 100

    # lambda with filter, map and reduce
    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

    print(list(filter(lambda x: x % 3 == 0, foo)))
    # filter() returns a filter object, from Py 3, list() return a list
    # print([x for x in foo if x % 3 == 0])
    # [18, 9, 24, 12, 27]

    print(list(map(lambda x: x * 2 + 10, foo)))
    # print [x * 2 + 10 for x in foo]
    # [14, 46, 28, 54, 44, 58, 26, 34, 64]

    print(functools.reduce(lambda x, y: x + y, foo))
    # reduce is in functools from Python 3.0
    # reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    # 139, sum of foo

    # compute prime numbers
    nums = range(2, 50)
    for i in range(2, 8):
        print('Loop:', i, type(nums), list(nums))
        nums = list(filter(lambda x: x == i or x % i, nums))
    print(nums)

    # for sort
    ids = [1, 2, 1, 2]
    aml = ['dog', 'cat', 'pig', 'bird']
    print(
        sorted(zip(ids, aml), key=lambda x: str(x[0])+x[1]))
    # not cmp parameter from Py 3
