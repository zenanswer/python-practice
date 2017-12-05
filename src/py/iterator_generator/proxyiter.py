#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Node:
    def __init__(self, value):
        self._value = value
        self._childern = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._childern.append(node)

    # return self._childern 's iter
    def __iter__(self):
        return iter(self._childern)


if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)
