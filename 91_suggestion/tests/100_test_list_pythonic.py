#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/10/17 18:36
# @Author: hlliu
from collections import defaultdict

'''
将d1 转化成： {'p': [1, 2, 3], 'h': [1, 2, 3]}
'''

d1 = [('p', 1), ('p', 2), ('p', 3), ('h', 1), ('h', 2), ('h', 3)]


def test_set_default():
    result = {}

    for (key, value) in d1:
        result.setdefault(key, []).append(value)

    print(result)


def test_default_dict():
    result = defaultdict(list)

    for (key, value) in d1:
        result[key].append(value)

    print(result)