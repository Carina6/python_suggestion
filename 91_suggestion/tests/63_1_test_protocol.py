#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 63：熟悉 Python 对象协议1
def test_protocol():
    class A(object):
        # 字符串格式化中，如果有占位符 %s，那么按照字符串转换的协议，Python 会自动地调用相应对象的 __str__() 方法
        # __repr__和__str__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员
        def __str__(self):
            print('calling __str__')
            return super(A, self).__str__()

        # 如果类中没有定义__str__, 则使用__repr__，实际上__str__只是覆盖了__repr__以得到更友好的用户显示
        def __repr__(self):
            print('calling __repr__')
            return super(A, self).__repr__()

        def __add__(self, other):
            print('calling __add__')

    class B(object):
        # __add__ 的反运算方法；所有数值运算符和位运算符都支持反运算，规则一律在前面加上r即可
        def __radd__(self, other):
            print('calling __radd__')

        # 可调用对象协议， 类似函数对象，能够让类实例表现得像函数一样
        def __call__(self, *args, **kwargs):
            print('calling __call__:{}'.format(args[0]))

        # 可哈希对象，用以支持hash()的内置函数；
        # 只有支持可哈希协议的类型才能作为dict的键类型，只要继承自object的新式类默认就支持
        def __hash__(self):
            print('calling __hash__')

    # 定义一个容器类，所需的协议；其实object类已经定义了这些协议，只要继承object的类
    class C(object):
        # 用来支持len()函数
        def __len__(self):
            print('calling __len__')
            return 1

        # 读
        def __getitem__(self, item):
            print('calling __getitem__')

        # 写
        def __setitem__(self, key, value):
            print('calling __setitem__')

        # 删
        def __delitem__(self, key):
            print('calling __delitem__')

        # 迭代器
        def __iter__(self):
            print('calling __iter__')

        # 倒序
        def __reversed__(self):
            print('calling __reversed__')

        # 支持in 和 not in
        def __contains__(self, item):
            print('calling __contains__')

    a = A()
    b = B()
    # 调用__str__
    print('%s' % a)
    print('{}'.format(a))

    a + b  # 反运算  调用A的__add__操作，如果没有，则调用B的__radd__操作
    b(222)  # 类B 定义了可调用协议__call__

    c = C()  # 容器类，
    # print(len(a))               # 报错，object of type 'A' has no len()
    c['test'] = a
    print(len(c))
