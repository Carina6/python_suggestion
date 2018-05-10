#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 51：用 mixin 模式让程序更加灵活
# 详细讲解： https://kevinguo.me/2018/01/19/python-topological-sorting/
def test_mixin():
    print()

    class A(object):
        def foo(self):
            print('a foo')

        def bar(self):
            print('a bar')

    class B(object):
        def foo(self):
            print('b foo')

        def bar(self):
            print('b bar')

    class C1(A):
        pass

    class C2(B):
        def bar(self):
            print('c2 bar')

    class D(C1, C2):  # 多重继承
        pass

    print(D.__mro__)  # 类D的继承顺序：D->C1->A->C2->B->object
    d = D()
    d.foo()  # 按继承顺序查找foo()方法，找到即输出
    d.bar()  # 同上
