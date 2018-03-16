#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Magic Methods and Operator Overloading
# https://www.python-course.eu/python3_magic_methods.php


class Length:

    __metric = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
                "in": 0.0254, "ft": 0.3048, "yd": 0.9144,
                "mi": 1609.344}

    def __init__(self, value, unit="m"):
        print("%s __init__" % id(self))
        self.value = value
        self.unit = unit

    def Converse2Metres(self):
        return self.value * Length.__metric[self.unit]

    def __add__(self, other):
        print("%s __add__ %s" % (id(self), id(other)))
        temp = self.Converse2Metres() + other.Converse2Metres()
        return Length(temp / Length.__metric[self.unit], self.unit)

    def __str__(self):
        print("%s __str__" % id(self))
        return str(self.Converse2Metres())

    def __repr__(self):
        print("%s __repr__" % id(self))
        return ("Length(" + str(self.value) + ", '" + self.unit + "')")


if __name__ == "__main__":
    x = Length(4)
    print("X is %s" % id(x))
    print("__str__ of X is %s" % x)
    print("__repr__ of X is %s" % repr(x))
    print("Type of X %s (ID %s) and Length %s" % (str(type(x)), id(x), str(x)))

    y = eval(repr(x))
    print("Y is %s" % id(y))
    print("Type of Y %s (ID %s) and Length %s" % (str(type(y)), id(y), str(y)))

    z = Length(4.5, "yd") + Length(1)
    print("Z is %s" % id(z))
    print("Type of Z %s (ID %s) and Length %s" % (str(type(z)), id(z), str(z)))
