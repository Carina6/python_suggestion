#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import threading
import urllib
from collections import Counter
from configparser import ConfigParser
from copy import deepcopy
from queue import Queue
from time import sleep, ctime
import os

from test import broker
from test.my_singleton import my_singleton
from test.utils.state import stateful, State, behavior, switch


# 23: 使用 else 子句简化循环（异常处理）
def test_prime():
    print()

    def print_prime(n):
        for i in range(2, n):
            for j in range(2, i):   # 正常循环完 执行else中的代码
                if i % j == 0:
                    break           # 不会执行else中的代码
            else:
                print('{} is a prime number'.format(i))

    print_prime(7)


# 26：深入理解 None，正确判断对象是否为空
def test_bool():
    print()
    l = []
    if l is not None:
        print('l is {}'.format(l))
    else:
        print('l is empty')

    if l:       # 调用对象 的__nonzero__() 方法，如果没有定义改方法，将会调用__len__()进行判断，如果两种都没定义，则返回true
        print('l is not empty')
    else:
        print('l is empty.')


# 37：按需选择 sort() 或者 sorted()
def test_sort():
    print()
    persons = [{'name': 'Jon', 'age': 32}, {'name': 'Alan', 'age': 50}, {'name': 'Bob', 'age': 23}]

    # sorted 根据指定key排序，此例根据name正序，age倒序排列，不会改变person列表的原始值
    persons_sorted = sorted(persons, key=lambda x: (x['name'], -x['age']))
    print(persons_sorted)

    # sort 根据指定key排序，不会改变person列表的原始值
    persons.sort(key=lambda x: (x['name'], -x['age']))
    print(persons)


# 32：警惕默认参数潜在的问题
# def test_report(when=time.time): # 而不是when=time.time()
#     print(when)
def test_default():
    print()

    # 陷阱：numbers 为可变参数，随着func函数的调用，一直添加num元素
    def func_e(numbers=[], num=1):
        numbers.append(num)
        return numbers
    print(func_e())
    print(func_e())

    # 正确使用
    def func_t(numbers=None, num=1):
        if numbers:
            numbers.append(num)
        else:
            numbers = [num]
        return numbers
    print(func_t())
    print(func_t())

    '''
    默认参数为可变参数的应用
    例：计算一个数的阶乘时可以用一个可变对象的字典当作缓存值来实现缓存，缓存中保存计算好的值，
    第二次调用的时候就无需重复计算，直接从缓存中拿
    '''
    def factorial(num, cache={}):
        if num == 0:
            return 1
        if num not in cache:
            print('xxx')
            cache[num] = factorial(num - 1) * num
        return cache[num]


# 34：深入理解 str() 和repr() 的区别
def test_str():
    s = '123'
    print(str(s))       # str()面向用户，返回用户友好和可读性强的字符串类型
    print(repr(s))      # repr()面向 Python 解释器或开发人员，返回 Python 解释器内部的含义


# 38：使用 copy 模块深拷贝对象
def test_copy():
    print()
    l = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    c = copy.copy(l)        # 浅拷贝，当拷贝的对象中有 可变对象 时，c和l的值的改变会互相影响
    f = id(l) == id(c)
    print(f)

    l['a'].append(4)
    c['b'].append(7)

    print('l='+str(l))
    print('c='+str(c))

    print('==========')

    dc = deepcopy(l)        # 深拷贝，不仅仅拷贝了原始对象自身，也对其包含的值进行拷贝，深拷贝产生的副本可以随意修改而不需要担心会引起原始值的改变
    f = id(l) == id(dc)
    print(f)

    l['a'].append(5)
    dc['b'].append(8)
    print('l='+str(l))
    print('dc='+str(dc))

    print('==========')
    a = [1, 2]
    b = [a, a]
    c = deepcopy(b)         #
    f1 = id(b[0]) == id(c[0])
    f2 = id(b[0]) == id(b[1])
    print(f1)
    print(f2)
    c[0].append(3)
    print(a)
    print(c)


# 39：使用 Counter 进行计数统计
def test_counter():
    some_data_list = ['a', '2', 2, 3, 5, 'c', '7', 4, 5, 'a', 'b']
    some_data_set = {'a', '2', 2, 3, 5, 'c', '7', 4, 5, 'a', 'b'}
    c = Counter(some_data_list)
    print(c)
    print(list(c.elements()))     # 获取 key 值 ['a', 'a', '2', 2, 3, 5, 5, 'c', '7', 4, 'b']
    print(c.most_common(2))       # 前 N 个出现频率最高的元素以及对应的次数 [('a', 2), (5, 2)]
    print(c['y'])                 # 访问不存在的元素, 返回 0

    s = 'sucess'
    sc1 = Counter(s)
    print(sc1)                     # Counter({'s': 3, 'u': 1, 'c': 1, 'e': 1})
    sc1.update('successfully')     # 更新统计值
    print(sc1)                     # Counter({'s': 6, 'u': 3, 'c': 3, 'e': 2, 'l': 2, 'f': 1, 'y': 1})
    sc1.subtract('successfully')   # 统计数相减，允许为0或为负
    print(sc1)                     # Counter({'s': 3, 'u': 1, 'c': 1, 'e': 1, 'f': 0, 'l': 0, 'y': 0})
    sc2 = Counter(s=3, c=2, e=1, u=1)
    print(Counter(sc2))


# 40：深入掌握 ConfigParser
def test_parser():
    print()
    conf = ConfigParser()
    conf.read('config.conf')
    print(conf.get('db1', 'conn_str'))  # db1中不存在的key，即用default中的值
    print(conf.get('db2', 'conn_str'))


# 43：一般情况下使用 ElementTree 解析 XML


# 48：使用 threading 模块编写多线程程序
def test_thread():
    print()

    def music(func):
        for i in range(2):
            print("I was listening to {}. {}".format(func, ctime()))
            sleep(5)  # 程序休眠 1 秒

    def move(func):
        for i in range(2):
            print("I was watching at the {}! {}".format(func, ctime()))
            sleep(1)

    threads = []
    t1 = threading.Thread(target=music, args=('爱情买卖',))
    threads.append(t1)
    t2 = threading.Thread(target=move, args=('阿凡达',))
    threads.append(t2)

    for t in threads:
        t.setDaemon(False)  # 声明线程为守护线程,true:表明主线程的退出可以不用等待子线程完成; false:所有的非守护线程结束后主线程才会结束
        t.start()
    t.join()                # 此方法能够阻塞当前上下文环境，直到调用该方法的线程终止或到达指定的 timeout
                            # for 循环中的t 非循环中的局部变量，是test_thread方法中的局部变量
    print("all over {}".format(ctime()))


'''
Queue.Queue(maxsize)：先进先出，maxsize 为队列大小，其值为非正数的时候为无限循环队列
Queue.LifoQueue(maxsize)：后进先出，相当于栈
Queue.PriorityQueue(maxsize)：优先级队列

常用方法:
Queue.qsize()：返回近似的队列大小。当该值 > 0 的时候并不保证并发执行的时候 get() 方法不被阻塞，同样，对于 put() 方法有效。
Queue.empty()：队列为空的时候返回 True，否则返回 False
Queue.full()：当设定了队列大小的情况下，如果队列满则返回 True，否则返回 False
Queue.put(item[, block[, timeout]])：往队列中添加元素 item，block 设置为 False 的时候，如果队列满则抛出 Full 异常。
如果 block 设置为 True，timeout 为 None 的时候则会一直等待直到有空位置，否则会根据 timeout 的设定超时后抛出 Full 异常
Queue.put_nowait(item)：等于 put(item, False)
Queue.get([block[, timeout]])：从队列中删除元素并返回该元素的值
Queue.get_nowait()：等价于 get(False)
Queue.task_done()：发送信号表明出列任务已经完成，经常在消费者线程中用到
Queue.join()：阻塞直至队列中所有的元素处理完毕

Queue 中的队列和 collections.deque 所表示的队列并不一样，前者用于不同线程之间的通信，内部实现了线程的锁机制，后者是数据结构上的概念，支持 in 方法。
'''
# 49：使用 Queue 使多线程编程更加安全
# Queue实现了所需要的锁，是线程安全的
def test_queue():
    class DownloadThread(threading.Thread):

        def __init__(self, queue):
            threading.Thread.__init__(self)
            self.queue = queue

        def run(self):
            while True:
                url = self.queue.get()
                print('{0} begin download {1}...'.format(self.name, url))
                self.download_file(url)
                self.queue.task_done()                                 # 发送信号表明出列任务已经完成
                print('{0} download completed!!!'.format(self.name))

        def download_file(self, url):               # 下载网页源码
            urlhandler = urllib.request.urlopen(url)
            fname = os.path.basename(url) + '.html'
            with open(fname, 'wb') as f:
                while True:
                    chunk = urlhandler.read(1024)
                    if not chunk: break
                    f.write(chunk)

    urls = ['http://wiki.python.org/moin/WebProgramming',
            'https://wiki.python.org/moin/BeginnersGuide',
            'http://wiki.python.org/moin/Documentation'
            ]
    queue = Queue()

    for i in range(2):
        t = DownloadThread(queue)    # 多个线程共享queue队列
        t.setDaemon(True)
        t.start()

    for url in urls:
        queue.put(url)
    queue.join()


# 50：利用模块实现单例模式
def test_singleton():
    print()
    s1 = my_singleton   # module 在程序中只被加载一次，本身是单例的
    s2 = my_singleton
    print(id(s1) == id(s2))  # 如果在不同的module中，s1和s2的id不相等


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

    class D(C1, C2):             # 多重继承
        pass

    print(D.__mro__)             # 类D的继承顺序：D->C1->A->C2->B->object
    d = D()
    d.foo()                      # 按继承顺序查找foo()方法，找到即输出
    d.bar()                      # 同上


# 52：用发布订阅模式实现松耦合
'''
发布者将消息分为不同类别直接发布，订阅者订阅并接受感兴趣的消息。一个中间代理人broker维护发布者和订阅者的关系
'''
def test_subscribe_mode():
    def greeting(name, n):
        print('hello,{}'.format(name))
    def bye(name, n):
        print('hello,{}'.format(n))
    broker.subscribe('greet', greeting)     # 参数为 主题 和 函数名
    broker.subscribe('greet', bye)
    broker.publish('greet', name='carinaliu', n='liu')    # 参数为 主题 和 函数参数


# 53：用状态模式美化代码
def test_state_mode():

    @stateful
    class User(object):
        # 退出状态类，定义退出状态时可进行的操作
        class signout(State):
            default = True       # 通过default 属性定义默认状态

            @behavior
            def signin(self, user, pwd):
                print('signin with user and pwd')
                switch(self, User.signin)

        # 登录状态类，定义登录状态时可进行的操作
        class signin(State):
            @behavior
            def move(self, dst):
                print(dst)

            @behavior
            def atk(self, other):
                print(other)

            @behavior
            def signout(self):
                print('signout!!')
                switch(self, User.signout)

    user = User()
    # user.move('move0')            # 默认状态为signout, 此时不能进行signin类中的操作（报错）
    user.signin('user', 'pwd')      # 调用此方法将状态转换为signin
    user.move('move1')              # 此时状态为signin， 可调用该类下的方法
    user.signout()                  # 状态转为signout
    # user.move('move2')            # 不能进行signin类中的操作（报错）


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
    print(a)                        # 类
    print(a())                      # 类实例
    print(a.bar)                    # 类调用属性
    b = a()                         # 创建实例对象
    print(b.bar)                    # 用实例对象调用属性 bar
    b.echo_bar()                    # 用实例对象调用函数 echo_bar
    print(b.__class__)              # __class__ 用来查看对象b 的类型
    print(b.__class__.__class__)    # type

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


# 59: 理解描述符机制
def test_discribe_protocol():
    class A(object):
        class_attr = 1

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


# 60：区别__getattr__()和__getattribute__()
# todo
def test_getattr():
    pass


# 63：熟悉 Python 对象协议
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

    a + b                         # 反运算  调用A的__add__操作，如果没有，则调用B的__radd__操作
    b(222)                        # 类B 定义了可调用协议__call__

    c = C()                       # 容器类，
    # print(len(a))               # 报错，object of type 'A' has no len()
    c['test'] = a
    print(len(c))




