#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def typed_property(name, expected_type):
    print('typed_property', name, expected_type)
    storage_name = '_' + name

    @property
    def prop(self):
        # self is a instance of "Person" class
        print('typed_property prop', self)
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        # self is a instance of "Person" class
        print('typed_property prop setter', self)
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type))
        setattr(self, storage_name, value)

    # return a property object
    return prop


# Example use
class Person:
    name = typed_property('name', str)
    age = typed_property('age', int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    p = Person('wang', 32)
    print('p.name:', p.name)
    print('p.age:', p.age)
    # p has no "name" and "age", just "_name" and "_age"
    # Person has name and age, both of them are "property object"
    # Note: here is not "prop" in class and instance
    print('vars(Person):\n', vars(Person))
    print('vars(p):\n', vars(p))
