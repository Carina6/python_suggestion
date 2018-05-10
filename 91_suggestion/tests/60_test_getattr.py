#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 60：区别__getattr__()和__getattribute__()
''' __getattribute__() 总会被调用，定义了__getattr__() 当AttributeError异常发生时会被调用
注意：
1.覆盖了__getattribute__()方法后，任何属性的访问都会调用用户定义的__getattribute__,性能上会有所损耗，比使用默认的方法要慢
2.覆盖的__getattr__()如果能动态处理事先未定义的属性，可以更好的实现数据隐藏，因为dir()通常只显示正常的属性和方法
'''


def test_getattr():
    class A(object):

        def __init__(self, name):
            self.name = name

        def __getattr__(self, name):
            print('calling __getattr__:', name)

        def __getattribute__(self, name):
            try:
                return super(A, self).__getattribute__(name)
            except KeyError:
                return 'default'

    a = A('attribute')
    print(a.name)
    # 未定义__getattr__时，调用__getattribute__()方法报错：AttributeError: 'A' object has no attribute 'test'
    # 定义__getattr__，报错AttributeError时，会调用__getattr__
    print(a.test)
