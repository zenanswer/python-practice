#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# http://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p13_using_mataclass_to_control_instance_creation.html#


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


# Example
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')


if __name__ == '__main__':
    print('Try to create one Spam')
    a = Spam()
    print('Try to create another Spam')
    b = Spam()
    if a is b:
        print('a and b are same.')
    else:
        pass
    print('Test done.')
