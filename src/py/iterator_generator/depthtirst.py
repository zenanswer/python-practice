#!/usr/bin/env python3
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

    def depth_first(self):
        # return self
        yield self
        # invoke self.__iter__
        for child in self:
            # 1. "yield from" Python3(PEP 380)
            yield from child.depth_first()


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for child in root.depth_first():
        # invoke Node.__repr__
        print(child)
