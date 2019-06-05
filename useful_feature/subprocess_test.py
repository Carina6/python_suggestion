#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-21 22:25
# @Author  : hlliu

import subprocess


def test_subprocess():
    '''
    ping 命令Windows和Linux有区别
    win：-c 路由隔离舱标识符
    linux: -c 回应次数
    '''
    process = subprocess.Popen("ping www.baidu.com", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = process.communicate()
    print(out)
    print(error)

    # subprocess.call()
    # res = process.wait()
    # print(type(res))
