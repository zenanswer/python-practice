#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from collections import deque


# search() has "yield", so it is a Generator
def search(f, pattern, history=5):
    # queue has a limit
    previous_lines = deque(maxlen=history)
    # iterator the file
    for line in f:
        if pattern in line:
            # send out
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('somefile.txt') as f:
        # iterator an Generator search()
        for line, previous_lines in search(f, 'python', 5):
            print('='*4 + ' match line ' + '='*4)
            print(line, end='')
            print('-'*4 + ' previous lines ' + '-'*4)
            for pline in previous_lines:
                print(pline, end='')
