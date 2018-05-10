#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 34：深入理解 str() 和repr() 的区别
def test_str():
    s = '123'
    print(str(s))  # str()面向用户，返回用户友好和可读性强的字符串类型
    print(repr(s))  # repr()面向 Python 解释器或开发人员，返回 Python 解释器内部的含义