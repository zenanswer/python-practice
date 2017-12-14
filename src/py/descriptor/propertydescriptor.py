#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class Typed:
    def __init__(self, name, excepted_type):
        self.name = name
        self.excepted_type = excepted_type

    def __get__(self, instance, cls):
        print('Typed __get__:', self, instance, cls)
        if instance is None:
            return self
        print('Typed __get__ instance.__dict__:', instance.__dict__)
        print('Typed __get__ cls.__dict__:', cls.__dict__)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.excepted_type):
            raise TypeError('Excepted ' + str(self.excepted_type))
        instance.__dict__[self.name] = value
        print('Typed __set__ instance.__dict__:', instance.__dict__)

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# here is a decorate on class,
# and add some attribute on this class
def typeassert(**kwargs):
    def decorate(cls):
        print('typeassert decorate:', cls)
        for name, excepted_type in kwargs.items():
            print('typeassert decorate:', name, excepted_type)
            # add "name = Typed()" on class,
            # just like "Integer" in "simpledescriptor.py"
            setattr(cls, name, Typed(name, excepted_type))
        return cls
    return decorate


@typeassert(first_name=str, last_name=str)
class Person:
    def __init__(self, first_name, last_name):
        # print('>>>Person __init__')
        # Invoke first_name.setter here
        self.first_name = first_name
        self.last_name = last_name
        print('>>>Person __init__', self.first_name, self.last_name)


if __name__ == '__main__':
    person = Person('F', 'L')
    print('main:', person.first_name, person.last_name)
    person.first_name = 123
