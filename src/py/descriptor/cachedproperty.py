#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class _Missing(object):
    def __repr__(self):
        return 'no value'

    def __reduce__(self):
        return '_missing'


_missing = _Missing()


class cached_property(object):
    def __init__(self, func, name=None, doc=None):
        print('cached_property(in):', func, name, doc)
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        # self.func = Foo.foo(instance)
        self.func = func
        print('cached_property(out):', func, self.__name__, self.__doc__)

    def __get__(self, obj, type=None):
        # "self", here is a instance of cached_property
        # "obj", the instance of "Foo" class
        # "type", type of "obj", "Foo" here
        print('cached_property __get__:', self, obj, type)
        print('self.__name__:', self.__name__)  # self.__name__ is "foo" here
        print('obj.__dict__:', obj.__dict__)
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, _missing)
        if value is _missing:
            # call Foo.foo(instance) here
            value = self.func(obj)
            # add a new attribute "foo" in to obj.__dict__
            obj.__dict__[self.__name__] = value
        print('obj.__dict__:', obj.__dict__)
        return value


class Foo(object):
    @cached_property
    def foo(self):
        '''
            Here a Foo.foo function for cached_property
        '''
        print('Foo foo:', self, ', and first calculate')
        result = 'this is result'
        return result


f = Foo()
# no () after f.foo below
print(f.foo)   # first calculate, call cached_property.__get__()
print(f.foo)   # call f.__dict__[foo]
