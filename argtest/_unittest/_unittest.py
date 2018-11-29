#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 11:04 PM
# @Author  : hlliu
import unittest


class TestA(unittest.TestCase):

    # 此类下的用例执行前执行一次
    def setUpClass(cls):
        pass

    # 此类下每个测试用例执行前都执行一次
    def setUp(self):
        pass

    # 此类下每个测试用例执行后都执行一次
    def tearDown(self):
        pass

    # 此类下的用例执行后执行一次
    def tearDownClass(cls):
        pass

    def test_1(self):
        pass

    def test_2(self):
        pass
