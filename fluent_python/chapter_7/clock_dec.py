#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/10/29 17:38
# @Author: hlliu

import time


def clock(func):
    print('call clock')
    def clocked(*args):
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('{}({})'.format(name, arg_str))
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked
