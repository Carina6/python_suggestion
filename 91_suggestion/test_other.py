#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
实例方法：
1.第一个参数一般写self（实例对象）
classmethod:
1.持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码;
2.第一个参数一般写cls(类对象)
staticmethod:
1.静态方法被用来组织类之间有逻辑关系的函数;
2.调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名
'''
def test_classmethod():

    class B(object):
        pass

    class A(B):
        # 实例对象的方法，只有类的实例才可以调用，self为隐式传入的实例对象
        def foo(self, x):
            print('executing foo({}, {})'.format(self, x))

        # 类方法，类和实例对象都可调用， cls为隐式传入的类对象
        @classmethod
        def class_foo(cls, x):
            print('executing class_foo({}, {})'.format(cls, x))

        # 静态方法， 类和实例对象都可调用， 无需传入 类对象/实例 参数
        @staticmethod
        def static_foo(x):
            print('executing static_foo({})'.format(x))

    a = A()
    print()
    a.foo(1)
    # A.foo(1)                      # 报错， 类对象不可调用类实例方法
    a.class_foo(2)
    A.class_foo(2)                  # 和前者一致
    a.static_foo(3)
    A.static_foo(3)                 # 和前者一致
