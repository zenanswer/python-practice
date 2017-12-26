#!/usr/bin/python
# -*- coding: UTF-8 -*-

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']

# i is started from 0 by default
for i, flavor in enumerate(flavor_list):
    print("%d:%s" % (i+1, flavor))

# set a start index for i, from 1 in this case
for i, flavor in enumerate(flavor_list, 1):
    print("%d:%s" % (i, flavor))
