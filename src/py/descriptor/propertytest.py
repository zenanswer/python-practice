#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class Person:
    def __init__(self, first_name):
        print('>>>Person __init__')
        # Invoke first_name.setter here
        self.first_name = first_name

    # Getter function
    # Greate a "property" instance - "first_name", and give a getter function.
    @property
    def first_name(self):
        print('>>>Person first_name Getter')
        return self._first_name

    # Setter function, for first_name
    @first_name.setter
    def first_name(self, value):
        print('>>>Person first_name Setter')
        if not isinstance(value, str):
            raise TypeError('Excepted a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        print('>>>Person first_name Deleter')
        raise AttributeError("Can't delete this attribute")


if __name__ == '__main__':
    person = Person('Bob')
    print('The first name is', person.first_name)
    person.first_name = 'Rob'
    print('The first name is', person.first_name)
    try:
        print('Try to set a int to first_name')
        person.first_name = 99
    except TypeError as e:
        print('TypeError here:\n', e)
    try:
        print('Try to delete first_name')
        del person.first_name
    except AttributeError as e:
        print('AttributeError here:\n', e)
    try:
        print('Try to init a Person with int')
        person = Person(25)
    except TypeError as e:
        print('TypeError here:\n', e)
