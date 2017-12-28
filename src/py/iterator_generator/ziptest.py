#!/usr/bin/python
# -*- coding: UTF-8 -*-

names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

max_letters = 0
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

# In Python 2.0 zip has some memory issue,
# using itertools.izip or itertools.izip_longest is better.

# In Python 3.0 zip_longest is under itertools.
