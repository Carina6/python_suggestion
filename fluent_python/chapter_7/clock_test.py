#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/10/29 17:40
# @Author: hlliu

import time

from fluent_python.chapter_7.clock_dec import clock


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


if __name__=='__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
