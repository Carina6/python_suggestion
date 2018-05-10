#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 65：熟悉 Python 的迭代器协议1
'''
1.实现__iter__()方法，返回一个迭代器
2.实现next()方法，返回当前的元素，并指向下一个元素的位置，如果当前位置已无元素，则抛出StopIteration异常
3.迭代器具有惰性求值的特性，可以在迭代至当前元素时才计算（或读取）该元素的值，非常适合遍历无穷个元素的集合
'''
def test_iter():
    class Fib(object):
        def __init__(self):
            self._a = 0
            self._b = 1

        def __iter__(self):
            return self

        def __next__(self):
            self._a, self._b = self._b, self._a+self._b
            return self._a

    # 对于一个可迭代的（iterable）/可遍历的对象，enumerate将其组成一个索引序列，利用它可以同时获得索引和值
    for i, f in enumerate(Fib()):
        if i > 10:
            break
        print(f)
