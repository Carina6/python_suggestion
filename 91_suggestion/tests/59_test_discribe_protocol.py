#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 59: 理解描述符机制
''' 实现了描述符协议__get__, __set__, __delete__ 的对象 称为描述符 '''


def test_discribe_protocol():
    class A(object):
        class_attr = 1

        # 每个函数都有__get__方法，也就是说每个函数都是描述符
        def my_method(self):
            print('my_method')

    # 每个类都有一个__dict__属性，包含类的所有属性，又称类属性
    print(A.__dict__)
    a = A()

    # 实例的属性，称实例属性
    print(a.__dict__)
    # 当我们通过实例访问某一个属性时，它会首先尝试在实例属性中查找，如果找不到，则会到类属性中查找
    print(a.class_attr)

    # 通过实例增加属性，只能是实例属性
    a.class_attr1 = 2
    # 通过类增加的属性，是类属性；但是内置类型不能随意增加属性或方法
    A.class_attr2 = 3

    print(A.__dict__['my_method'])

    print(A.my_method)