#!/usr/bin/env python
# -*- coding: utf-8 -*-
from re import findall

from pipe import add, take_while, where, Pipe, groupby, select, sort, count


# 64：利用操作符重载实现中缀语法
'''Pipe的使用'''
def test_pipe():
    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    # 计算小于4000000的斐波那契数中的偶数之和
    amount = fib() | where(lambda x: x % 2 == 0) | take_while(lambda x: x < 4000000) | add()
    print(amount)

    # 读取文件，统计文件中每个单词出现的次数，然后按照次数从高到低对单词排序
    with open('argparse.py') as f:
        fs = f.read()
        print(findall('\w+', fs))
        print(fs
              | Pipe(lambda x: findall('\w+', x))
              # | Pipe(lambda x: (i for i in x if i.strip()))
              | groupby(lambda x: x)
              | select(lambda x: (x[0], (x[1] | count)))
              | sort(key=lambda x: x[1], reverse=True)
              )
