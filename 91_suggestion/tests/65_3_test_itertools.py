#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import product, permutations, combinations, combinations_with_replacement


# 65：熟悉 Python 的迭代器协议3
# 组合函数
def test_itertools2():

    print()
    # 计算m个序列的n次笛卡尔积
    print(list(product('ABCD', repeat=2)))

    print('1===============')
    # 产生全排列
    print(list(permutations('ABCD', 4)))

    print('2===============')
    # 产生无重复元素的组合
    # print(list(combinations('ABCD', 2)))
    print(set(combinations([-1, 0, 1, 2, -1, -4], 3)))
    print(list(combinations([-1, 0, 1, 2, -1, -4], 3)))

    print('3===============')
    # 产生有重复元素的组合
    print(list(combinations_with_replacement('ABCD', 2)))