#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/4/1 17:48
# @Author: hlliu
from functools import reduce
import requests

'''
map() & reduce() & filter()
'''


def add(x, y):
    return x + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits.get(s)


def fn(x, y):
    return x*10+y


def is_odd(n):
    return n % 2 == 1


'''
map(func, iterables)
'''
print(list(map(str, [1, 2, 3, 4, 5, 6])))

'''
reduce(func, iterables) =>1234
'''
print(reduce(fn, map(char2num, '1234')))

'''
filter
'''
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
