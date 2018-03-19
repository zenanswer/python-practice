#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# A Guide to Python's Magic Methods
# Rafe Kettler
# https://rszalski.github.io/magicmethods/

from functools import wraps


def log_method(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(
            'Method: %s ' % func)
        return func(*args, **kwargs)
    return wrapper


class FunctionalList:
    '''A class wrapping a list with some extra functional magic, like head,
    tail, init, last, drop, and take.'''

    @log_method
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    # len(self)
    @log_method
    def __len__(self):
        return len(self.values)

    # self[key]
    @log_method
    def __getitem__(self, key):
        # if key is of invalid type or value,
        # the list values will raise the error
        return self.values[key]

    # self[key] = val
    @log_method
    def __setitem__(self, key, value):
        self.values[key] = value

    # del self[key]
    @log_method
    def __delitem__(self, key):
        del self.values[key]

    # for x in self
    @log_method
    def __iter__(self):
        return iter(self.values)

    @log_method
    def __reversed__(self):
        return FunctionalList(reversed(self.values))

    @log_method
    def __str__(self):
        return ".".join([str(x) for x in self.values])

    def append(self, value):
        self.values.append(value)

    def head(self):
        # get the first element
        return self.values[0]

    def tail(self):
        # get all elements after the first
        return self.values[1:]

    def init(self):
        # get elements up to the last
        return self.values[:-1]

    def last(self):
        # get last element
        return self.values[-1]

    def drop(self, n):
        # get all elements except first n
        return self.values[n:]

    def take(self, n):
        # get first n elements
        return self.values[:n]


if __name__ == "__main__":
        fl = FunctionalList([1, 2, 3])
        print('Length:' + str(len(fl)))
        print('Reversed:' + str(reversed(fl)))
