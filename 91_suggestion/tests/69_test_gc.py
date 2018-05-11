#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gc


# 建议 69：对象的管理与垃圾回收
def test_gc():
    print()
    # gc的自动回收功能
    print(gc.isenabled())
    # 查看默认阈值
    print(gc.get_threshold())
    # gc.garbage 返回的是由于循环引用而产生的不可达的垃圾对象的列表
    print(gc.garbage)