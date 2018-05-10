#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ftplib import FTP


# 63：熟悉 Python 对象协议2
def test_closer():
    # 上下文管理协议，也就是对with语句的支持，通过__enter__和__exit__两个方法实现对资源的清理
    '''
    通过with语句和一个close方法来关闭一个对象
    与这里Closer类似的类在标准库已经存在，就是contextlib里的closing
    '''

    class Closer(object):
        def __init__(self, obj):
            self.obj = obj

        def __enter__(self):
            return self.obj

        def __exit__(self, exc_type, exc_val, exc_tb):
            try:
                self.obj.close()
            except AttributeError:
                print('Not closable.')
                return True

    ftp = FTP('ftp.byfly.by')
    ftp.login()
    with Closer(ftp) as conn:
        co = conn
        conn.dir()

    # co.dir()                   # 报错，因为此时FTP连接会话已经关闭
