#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a = [x for x in range(1, 11)]
print(a)

# squares = map(lambda x: x **2 ,a)
squares = [x*x for x in a]
print(squares)

# alt = map(lambda x: x**2, filter(lambda x: x%2==0,a))
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

# Dict still supports list comperehensions
chile_rank = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_rank.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)

# multilayer
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
#      [x (for row in matrix) for x in row]
print(flat)
# [ 1, 2, 3, 4, 5, 6, 7, 8, 9]

squared = [[x**2 for x in row] for row in matrix]
print(squared)
# [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

my_lists = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    # ...
]
flat = [x for sublist in my_lists
        for sublist2 in sublist
        for x in sublist2]
# (for sublist in my_lists)->sublist from my_lists
# (for sublist2 in sublist)->sublist2 from sublist
# x for x in sublist2 -> x from sublist2
print(flat)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
print(filtered)
# [[6],[9]]
