#!/usr/bin/env python
# -*- coding: utf-8 -*-
from configparser import ConfigParser


# 40：深入掌握 ConfigParser
def test_parser():
    print()
    conf = ConfigParser()
    conf.read('config.conf')
    print(conf.get('db1', 'conn_str'))  # db1中不存在的key，即用default中的值
    print(conf.get('db2', 'conn_str'))