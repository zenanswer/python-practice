#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class MyDescriptor():
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving[%s]: %s, obj %s, objtype %s' % (self, self.name, obj, objtype))
        return self.val

    def __set__(self, obj, val):
        print('Updating[%s]: %s, obj: %s, val: %s' % (self, self.name, obj, str(val)))
        self.val = val


if __name__ == "__main__":

    class MyClass():
        x = MyDescriptor(10, 'var x')
        y = MyDescriptor(20, 'var y')
        z = MyDescriptor(99, 'var z')

        def __init__(self, x, y):
            print('Init x: %d, y: %d' % (x, y))
            self.x = x
            self.y = y
            self.zz = 0

    mc = MyClass(30, 40)
    mc2 = MyClass(40, 30)
    print('X test:')
    print(mc.__dict__)
    print(mc.x)
    mc.x = 11
    print(mc.__dict__)
    print(mc.x)
    print('Y test:')
    print(mc.__dict__)
    print(mc.y)
    mc.y = 21
    print(mc.__dict__)
    print(mc.y)
    print('Z test:')
    print(MyClass.__dict__)
    print(MyClass.z)
    print(mc.z)
    MyClass.z = 100
    print(MyClass.__dict__)
    print(MyClass.z)
    print(mc.__dict__)
