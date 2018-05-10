#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 55：__init__()不是构造方法
'''
1.创建类的实例时调用__new__(), 需要返回类的对象，当返回类的对象的时候自动调用__init__()进行初始化
2.实例初始化时，调用__init__()
3.当子类继承自不可变类型（str,int,unicode,frozenset等）时，需要覆盖__new__()
4.作为用来初始化的 __init__() 方法在多继承的情况下，子类的 __init__()方法如果不显式调用父类的 __init__() 方法，则父类的 __init__() 方法不会被调用
5.通过super(子类， self).__init__()显式调用父类的初始化方法
'''


def test_init():
    # 创建一个集合能够将任何以空格隔开的字符串变为集合中的元素
    class UserSet(frozenset):
        def __new__(cls, args):
            if args and isinstance(args, str):
                args = (args.split(),)
            return super(UserSet, cls).__new__(cls, *args)

    us = UserSet('hello world world python!')
    print(us)