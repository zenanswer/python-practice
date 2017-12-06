#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# https://docs.python.org/3/library/itertools.html

import itertools


items = ['a', 'b', 'c']

print('itertools.permutations:')
# ('a', 'b', 'c')
# ('a', 'c', 'b')
# ('b', 'a', 'c')
# ('b', 'c', 'a')
# ('c', 'a', 'b')
# ('c', 'b', 'a')
for p in itertools.permutations(items):
    print(p)

print('itertools.permutations(2 in 3):')
# ('a', 'b')
# ('a', 'c')
# ('b', 'a')
# ('b', 'c')
# ('c', 'a')
# ('c', 'b')
for p in itertools.permutations(items, 2):
    print(p)

print('itertools.combinations:')
# ('a', 'b', 'c')
for p in itertools.combinations(items, 3):
    print(p)

print('itertools.combinations(2 in 3):')
# ('a', 'b')
# ('a', 'c')
# ('b', 'c')
for p in itertools.combinations(items, 2):
    print(p)
