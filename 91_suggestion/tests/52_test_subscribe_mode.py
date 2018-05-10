#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 52：用发布订阅模式实现松耦合
'''
发布者将消息分为不同类别直接发布，订阅者订阅并接受感兴趣的消息。一个中间代理人broker维护发布者和订阅者的关系
'''


def test_subscribe_mode():
    def greeting(name, n):
        print('hello,{}'.format(name))

    def bye(name, n):
        print('hello,{}'.format(n))

    broker.subscribe('greet', greeting)  # 参数为 主题 和 函数名
    broker.subscribe('greet', bye)
    broker.publish('greet', name='carinaliu', n='liu')  # 参数为 主题 和 函数参数