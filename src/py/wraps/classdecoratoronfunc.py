#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class logging(object):
    def __init__(self, func):
        print("[DEBUG]: logging __init__ {func}()".format(func=func.__name__))
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[DEBUG]: enter function {func}()".format(
            func=self.func.__name__))
        return self.func(*args, **kwargs)


@logging
def say(something):
    print("say {}!".format(something))


if __name__ == '__main__':
    say('>Here is something to say.<')
    say('>Here is something to say(2nd).<')
