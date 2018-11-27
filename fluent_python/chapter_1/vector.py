#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/10/29 16:11
# @Author: hlliu
from math import hypot


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


def test_vector1():
    v1 = Vector(3, 4)
    v2 = Vector(4, 6)
    print(v1 + v2)

    print(v1 * 3)
    print(abs(v1))
