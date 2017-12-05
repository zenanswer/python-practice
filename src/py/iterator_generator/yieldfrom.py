#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Python3(PEP 380) - yield from
# https://wenkefendou.gitbooks.io/python3-learning/content/yield_from.html


def yieldfromtworange(x):
    # get the value from another generator - range(x, 0, -1)
    yield from range(x, 0, -1)
    # get the value from range(x)
    yield from range(x)


def sub_generator():
    tally = 0
    while 1:
        next_value = yield
        if next_value is None:
            # if got None, then finish this sub_generator,
            # and return the tally count
            return tally
        tally += next_value


def main_generator(tallies):
    while 1:
        tally = yield from sub_generator()
        tallies.append(tally)


if __name__ == '__main__':

    print(list(yieldfromtworange(5)))

    tallies = []
    acc = main_generator(tallies)
    # start the main generator
    next(acc)
    # send 5 and 6
    acc.send(5)
    acc.send(6)
    # next_value is None, so 1st sub_generator is finished
    # and tally will be append into the list
    next(acc)
    acc.send(10)
    acc.send(30)
    next(acc)
    print(tallies)
