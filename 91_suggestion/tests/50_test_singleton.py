#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 50：利用模块实现单例模式
def test_singleton():
    print()
    # s1 = my_singleton  # module 在程序中只被加载一次，本身是单例的
    # s2 = my_singleton
    # print(id(s1) == id(s2))  # 如果在不同的module中，s1和s2的id不相等