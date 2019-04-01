#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/11/30 14:09
# @Author: hlliu


def outer():
    a = 0
    b = 1

    def inner():
        print(a)
        print(b)

        # b += 1        # A
        b = 4  # B
    inner()

outer()
