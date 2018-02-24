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
from test.MySingleton import my_singleton


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
