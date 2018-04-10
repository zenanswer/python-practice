#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class TestMetaClass(type):
    def __init__(self, *args, **kwargs):
        print(
            'TestMetaClass __init__ \nargs[%s] \nkwargs[%s]'
            % (args, kwargs))
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print(
            'TestMetaClass __call__ \nargs[%s] \nkwargs[%s]'
            % (args, kwargs))
        return super().__call__(*args, **kwargs)


class Test(metaclass=TestMetaClass):
    def __init__(self, *args, **kwargs):
        print('Test __init__ \nargs[%s] \nkwargs[%s]' % (args, kwargs))


if __name__ == '__main__':
    print('==== Before call Test class init')
    t = Test('p1_val', p2='p2_val')
    print('==== After call Test class init')
