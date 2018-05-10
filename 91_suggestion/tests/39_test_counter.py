#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import Counter


# 39：使用 Counter 进行计数统计
def test_counter():
    some_data_list = ['a', '2', 2, 3, 5, 'c', '7', 4, 5, 'a', 'b']
    some_data_set = {'a', '2', 2, 3, 5, 'c', '7', 4, 5, 'a', 'b'}
    c = Counter(some_data_list)
    print(c)
    print(list(c.elements()))  # 获取 key 值 ['a', 'a', '2', 2, 3, 5, 5, 'c', '7', 4, 'b']
    print(c.most_common(2))  # 前 N 个出现频率最高的元素以及对应的次数 [('a', 2), (5, 2)]
    print(c['y'])  # 访问不存在的元素, 返回 0

    s = 'sucess'
    sc1 = Counter(s)
    print(sc1)  # Counter({'s': 3, 'u': 1, 'c': 1, 'e': 1})
    sc1.update('successfully')  # 更新统计值
    print(sc1)  # Counter({'s': 6, 'u': 3, 'c': 3, 'e': 2, 'l': 2, 'f': 1, 'y': 1})
    sc1.subtract('successfully')  # 统计数相减，允许为0或为负
    print(sc1)  # Counter({'s': 3, 'u': 1, 'c': 1, 'e': 1, 'f': 0, 'l': 0, 'y': 0})
    sc2 = Counter(s=3, c=2, e=1, u=1)
    print(Counter(sc2))