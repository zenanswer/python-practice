#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

name, email, *phone_numbers = record
print('Name:%s Email:%s Phone Numbers:%s' % (name, email, phone_numbers))

name, email, *_ = record
print('Name:%s Email:%s' % (name, email))

name, _, *phone_numbers = record
print('Name:%s Phone Numbers:%s' % (name, phone_numbers))
