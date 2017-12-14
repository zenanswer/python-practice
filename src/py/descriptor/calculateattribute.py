#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    c = Circle(4)
    print('Radius:', c.radius)
    # no () here
    # invoke the getter func of property area,diameter and perimeter
    print('Area:', c.area)
    print('Diameter:', c.diameter)
    print('Perimeter:', c.perimeter)
