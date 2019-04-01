#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/4/1 16:58
# @Author: hlliu
import functools

'''
设计模式中，Java的装饰器模式需要通过继承和多态来实现

Python中
直接从语法层支持decorator，Python的decorator可以用函数实现，也可以用类实现

装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，
装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
'''

def log(func):
    # 添加此参数，以保证原函数名不变
    @functools.wraps(func)
    def wraper(*args, **kwargs):
        print('begin call')
        res = func(*args, **kwargs)
        print('end call')
        return res
    return wraper


def logger(params):
    def _log(func):
        @functools.wraps(func)
        def wraper(*args, **kwargs):
            print('begin call-{}'.format(params))
            res = func(*args, **kwargs)
            print('end call-{}'.format(params))
            return res
        return wraper
    return _log


@log
def f():
    pass


@logger('execute')
def f1():
    return 32


if __name__ == '__main__':
    f()
    print(f1())