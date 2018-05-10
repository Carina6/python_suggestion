#!/usr/bin/env python
# -*- coding: utf-8 -*-


import copy
from copy import deepcopy


# 38：使用 copy 模块深拷贝对象
def test_copy():
    print()
    l = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    c = copy.copy(l)  # 浅拷贝，当拷贝的对象中有 可变对象 时，c和l的值的改变会互相影响
    f = id(l) == id(c)
    print(f)

    l['a'].append(4)
    c['b'].append(7)

    print('l=' + str(l))
    print('c=' + str(c))

    print('==========')

    dc = deepcopy(l)  # 深拷贝，不仅仅拷贝了原始对象自身，也对其包含的值进行拷贝，深拷贝产生的副本可以随意修改而不需要担心会引起原始值的改变
    f = id(l) == id(dc)
    print(f)

    l['a'].append(5)
    dc['b'].append(8)
    print('l=' + str(l))
    print('dc=' + str(dc))

    print('==========')
    a = [1, 2]
    b = [a, a]
    c = deepcopy(b)  #
    f1 = id(b[0]) == id(c[0])
    f2 = id(b[0]) == id(b[1])
    print(f1)
    print(f2)
    c[0].append(3)
    print(a)
    print(c)
