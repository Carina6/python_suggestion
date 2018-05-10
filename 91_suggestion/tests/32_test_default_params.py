#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 32：警惕默认参数潜在的问题
# def test_report(when=time.time): # 而不是when=time.time()
#     print(when)
def test_default():
    print()

    # 陷阱：numbers 为可变参数，随着func函数的调用，一直添加num元素
    def func_e(numbers=[], num=1):
        numbers.append(num)
        return numbers

    print(func_e())
    print(func_e())

    # 正确使用
    def func_t(numbers=None, num=1):
        if numbers:
            numbers.append(num)
        else:
            numbers = [num]
        return numbers

    print(func_t())
    print(func_t())

    '''
    默认参数为可变参数的应用
    例：计算一个数的阶乘时可以用一个可变对象的字典当作缓存值来实现缓存，缓存中保存计算好的值，
    第二次调用的时候就无需重复计算，直接从缓存中拿
    '''

    def factorial(num, cache={}):
        if num == 0:
            return 1
        if num not in cache:
            print('xxx')
            cache[num] = factorial(num - 1) * num
        return cache[num]