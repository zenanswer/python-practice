#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from functools import partial


def printsomething(first="1st", second="2nd"):
    print(first, second)


fixsecondprint = partial(printsomething, second="3rd")

printsomething("99")
# 99 2nd, second is the default value

fixsecondprint("99")
# 99 3rd, second is fixed by functools.partial

fixfirstprint = partial(printsomething, "4th")

fixfirstprint("100")
# 4th 100

errorprint = partial(printsomething, notthis="not this")

errorprint("", "")
# TypeError: printsomething() got an unexpected keyword argument 'notthis'
