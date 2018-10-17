#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from configparser import ConfigParser

from os import path

ROOT_PATH = os.path.abspath(os.path.join(os.getcwd(), ".."))
conf = ConfigParser()


# 40：深入掌握 ConfigParser
def test_parser():
    print()
    conf.read(path.join(ROOT_PATH, 'config.conf'))
    print(conf.get('db1', 'conn_str'))  # db1中不存在的key，即用default中的值
    print(conf.get('db2', 'conn_str'))