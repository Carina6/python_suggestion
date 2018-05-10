#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 62：掌握 metaclass
'''
动态语言和静态语言的区别：函数和类的定义，不是编译时定义的，而是运行时动态创建的

元类用来创建类对象的，是类的类，type是Python的內建元类，
构建类时，可用__metaclass__定义元类，如果缺省，则使用默认的type元类

作用：
1. 拦截类的创建
2. 修改类
3. 返回修改之后的类

更具体的应用参见 OrmWithMetaclass.py
'''


def test_metaclass():
    def echo_bar(self):
        print(self.bar)

    # 使用class关键字时，Python幕后的做的事情是 通过type创建类
    # type(类名, 父类的元组（针对继承的情况，可以为空），包含 属性/函数 的字典（名称和值）)
    a = type('myclass', (), {'bar': True, 'echo_bar': echo_bar})
    print(a)  # 类
    print(a())  # 类实例
    print(a.bar)  # 类调用属性
    b = a()  # 创建实例对象
    print(b.bar)  # 用实例对象调用属性 bar
    b.echo_bar()  # 用实例对象调用函数 echo_bar
    print(b.__class__)  # __class__ 用来查看对象b 的类型
    print(b.__class__.__class__)  # type

    def upper_attr(class_name, class_parent, class_attr):
        attrs = ((name, value) for name, value in class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type(class_name, class_parent, uppercase_attr)

    class UpperAttrMetaclass(type):
        def __new__(cls, class_name, class_parent, class_attr):
            attrs = ((name, value) for name, value in class_attr.items() if not name.startswith('__'))
            uppercase_attr = dict((name.upper(), value) for name, value in attrs)
            return super(UpperAttrMetaclass, cls).__new__(cls, class_name, class_parent, uppercase_attr)

    class Foo(object, metaclass=UpperAttrMetaclass):
        # 经测试，通过__metaclass__设置无效，可在类参数中指定
        # __metaclass__ = UpperAttrMetaclass        # 使用类当元类
        # __metaclass__ = upper_attr                # 使用函数当元类
        bar = 'bip'

    print(hasattr(Foo, 'bar'))
    print(hasattr(Foo, 'BAR'))
    f = Foo()
    print(f.BAR)