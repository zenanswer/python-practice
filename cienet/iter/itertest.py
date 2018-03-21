#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class IterableGetItem():
    def __init__(self, alist=None):
        self.list = alist

    def __getitem__(self, i):
        print('__getitem__ index:' + str(i))
        if i >= len(self.list) or i < 0:
            raise IndexError('IndexError in IterableGetItem')
        return self.list[i]


class IterableIter():
    def __init__(self, alist=None):
        self.list = alist

    def __iter__(self):
        print('__iter__')
        return iter(self.list)


class IteratorNext():
    def __init__(self, alist=None):
        self.list = alist
        self.index = -1 if alist is None else 0

    def __iter__(self):
        print('__iter__')
        return self

    def __next__(self):
        print('__next__ index:%d' % self.index)
        if self.index >= len(self.list) or self.index < 0:
            raise StopIteration('StopIteration in IteratorNext')
        self.index += 1
        return self.list[self.index]


def test_func(myiter_obj):
    print('+'*5 + repr(myiter_obj) + '+'*5)

    def myforloop(myiter):
        for x in myiter:
            print(x)

    def myprint(myiter):
        print(myiter[9])

    def run_get_exception(myaction, myiter):
        try:
            myaction(myiter)
        except IndexError as exp:
            print('Got IndexError Exception:' + str(exp))
        except StopIteration as exp:
            print('Got StopIteration Exception:' + str(exp))
        except TypeError as exp:
            print('Got TypeError Exception:' + str(exp))

    run_get_exception(myforloop, myiter_obj)
    run_get_exception(myprint, myiter_obj)


if __name__ == "__main__":
    test_func(IterableGetItem([1, 2, 3, 4, 5]))
    test_func(IterableIter([1, 2, 3, 4, 5]))
    test_func(IteratorNext([1, 2, 3, 4, 5]))
