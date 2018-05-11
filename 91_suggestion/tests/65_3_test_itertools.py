#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import product, permutations, combinations, combinations_with_replacement


# 65：熟悉 Python 的迭代器协议3
# 组合函数
def test_itertools2():

    # 计算m个序列的n次笛卡尔积
    print(list(product('ABCD', repeat=2)))

    # 产生全排列
    print(list(permutations('ABCD', 2)))

    # 产生无重复元素的组合
    print(list(combinations('ABCD', 2)))

    # 产生有重复元素的组合
    print(list(combinations_with_replacement('ABCD', 2)))