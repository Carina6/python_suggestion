#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/4/1 18:16
# @Author: hlliu
import threading
import time


def loop():
    print('thread {} is running'.format(threading.current_thread().name))
    n = 0
    while n < 5:
        n += 1
        time.sleep(1)


t = threading.Thread(target=loop, name='loopThread')
t.start()
t.join()
