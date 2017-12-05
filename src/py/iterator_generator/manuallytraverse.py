#!/usr/bin/python
# -*- coding: UTF-8 -*-


def manaul_iter():
    print('manaul_iter')
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                if line is None:
                    break
                print(line)
        except StopIteration:
            print('Got StopIteration Exception')
            pass


def sample_case():
    print('sample_case')
    items = [1, 2, 3, 4, 5]
    # items.__iter__
    it = iter(items)
    while True:
        try:
            # it.__next__
            value = next(it)
            print(value)
        except StopIteration:
            print('Got StopIteration Exception')
            break


if __name__ == '__main__':
    manaul_iter()
    sample_case()
