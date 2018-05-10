#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import zip_longest, islice, starmap, tee

import itertools


'''itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算'''


# 65：熟悉 Python 的迭代器协议2
def test_itertools1():
    # count(start,step)会创建一个无限序列，类似的还有cycle(),repeat()
    natuals = itertools.count(1)

    # takewhile()用来根据条件判断来截取出一个有限的序列
    ns = itertools.takewhile(lambda x: x <= 10, natuals)
    print(list(ns))

    # dropwhile(assert，iterator) 过滤iterator中assert为true的值，知道遇到assert为false的值时停止，输出之后所有值
    print(list(itertools.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])))

    # takewhile(assert, iterator) 与dropwhile相反，遇到assert为false的值时停止，输出之前所有值
    print(list(itertools.takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))

    # filterfalse(assert, iterator) 刷选assert为false的值
    print(list(itertools.filterfalse(lambda x: x > 5, [6, 7, 8, 9, 1, 2, 3, 10])))

    # islice(iterator, n) 用来控制iterator的输出，迭代n次后停止
    print(list(islice(itertools.count(10), 5)))

    # chain() 可以把一组迭代对象串联起来，形成一个更大的迭代器
    for c in itertools.chain([1, 2, 3], ['a', 'b', 'c']):
        print(c)

    # tee(iterator, n=2) 类似复制的功能；n默认为2，且不可更改，所以返回两个迭代器，且相同
    i1, i2 = tee('ABCDE')
    for i in i1:
        print(i)

    # zip_longest(*iterator, fillvalue) 用于将多个迭代对象配对，如果长度不同，会使用fillvalue填充
    for item in zip_longest('ABCD', 'xy', '123456', fillvalue='blank'):
        print(item)

    def add(a, b):
        return a + b

    # starmap(function， iterator), 以iterator的值为参数，计算函数function的值
    for item in starmap(add, [(2, 3), (6, 7)]):
        print(item)

    # groupby() 把迭代器中相邻的重复元素挑出来放在一起,
    ''' 如果希望效果达到和sql中的一样，需要先将list排序一下， Pipe中的groupby实现了此功能'''
    for key, group in itertools.groupby('AAABBBCCAAA'):
        print(key, list(group))
