#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict

'''
订阅模式的中间代理人，维护发布者和订阅者的关系，
订阅者把感兴趣的主题告诉它，而发布者的信息也通过它路由到各个订阅者处。
'''

route_table = defaultdict(list)


# 订阅
def subscribe(topic, callback):
    if callback in route_table[topic]:
        return
    route_table[topic].append(callback)


# 发布
def publish(topic, *args, **kw):
    for func in route_table[topic]:
        func(*args, **kw)

