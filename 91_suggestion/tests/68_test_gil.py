#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 建议 68：理解 GIL 的局限性
'''
GIL被称为全局解释器锁，是Python虚拟机上用作互斥线程的一种机制，
他的作用是保证任何情况下虚拟机中只会有一个线程被运行，而其他线程都处于等待GIL锁被释放的状态
'''
def test_gil():
    pass