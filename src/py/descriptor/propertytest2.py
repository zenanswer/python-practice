#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Here are two attribute first_name and last_name


class Person:
    def __init__(self, first_name, last_name):
        print('>>>Person __init__')
        self.first_name = first_name
        self.last_name = last_name

    def __setattr__(self, name, value):
        if (name == 'first_name' or name == 'last_name'):
            if not isinstance(value, str):
                raise TypeError('Excepted a string')
        self.__dict__[name] = value


if __name__ == '__main__':
    person = Person('F', 'L')
    print('Last Name:', person.last_name)
    person.last_name = 'L2'
    print('Last Name:', person.last_name)
    person.last_name = 112
