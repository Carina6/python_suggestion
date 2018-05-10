#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 26：深入理解 None，正确判断对象是否为空
def test_bool():
    print()
    l = []
    if l is not None:
        print('l is {}'.format(l))
    else:
        print('l is empty')

    if l:  # 调用对象 的__nonzero__() 方法，如果没有定义改方法，将会调用__len__()进行判断，如果两种都没定义，则返回true
        print('l is not empty')
    else:
        print('l is empty.')