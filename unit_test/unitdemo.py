#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-05 22:35
# @Author  : hlliu
import unittest


def add(x, y):
    return x + y


class add_test(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
