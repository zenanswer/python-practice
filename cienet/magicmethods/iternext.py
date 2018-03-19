#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# A Guide to Python's Magic Methods
# Rafe Kettler
# https://rszalski.github.io/magicmethods/

from behindcontainer import FunctionalList


if __name__ == "__main__":
    fl = FunctionalList([1, 2, 3, 4, 5])
    print('for test:')
    for item in fl:
        print(item)

    print('next test:')
    it = iter(fl)
    while True:
        try:
            x = next(it)
            print(x)
        except StopIteration:
            break
