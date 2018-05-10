#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 23: 使用 else 子句简化循环（异常处理）
def test_prime():
    print()

    def print_prime(n):
        for i in range(2, n):
            for j in range(2, i):  # 正常循环完 执行else中的代码
                if i % j == 0:
                    break  # 不会执行else中的代码
            else:
                print('{} is a prime number'.format(i))

    print_prime(7)