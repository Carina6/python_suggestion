#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 10:35 PM
# @Author  : hlliu
import argparse


def main():
    ''' description : 给整个参数解析定义帮助文档 '''
    parser = argparse.ArgumentParser(description="learn argparser")
    ''' 定位参数， 默认必选， 不用带-即可用，按位置来取参数值 '''
    # parser.add_argument("echo")

    '''
    可选参数，通过- 或 -- 来指定短/长参数，可同时存在，也可只存在一个，以下命令，参数值保存在args.verbosity参数中
    action: 
        - store: 默认action模式，存储值到指定变量
        - store_const: 存储值在参数的const部分指定，多用于实现非布尔的命令行flag
        - store_true / store_false :布尔开关。可以2个参数对应一个变量, 不指定参数也可执行
        - append:存储值到列表，该参数可以重复使用
        - append_const:存储值到列表，存储值在参数的const部分指定
        - count:统计参数简写输入的个数
        - version:输出版本信息然后退出。
    type: 指定参数类型，不能转换为此类型则会报错
    choice: 限定参数可选值
    default: 默认值
    '''
    parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], default=1, help="increase output verbosity")

    ''' 互斥参数， q, l 为互斥参数，可定义多个互斥组 '''
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-q", "--quiet", action="store_true")
    group.add_argument("-l", "--loud", action="store_true")

    ''' 定义二级命令解析器 '''
    subparsers = parser.add_subparsers(help="sub parser help")

    ''' 定义二级命令 a ,并添加二级命令的可选参数 -x'''
    parser_a = subparsers.add_parser("a", help="a parser help")
    parser_a.add_argument("-x", type=int, help="x help")

    ''' 定义二级命令 b ,并添加二级命令的可选参数 -y'''
    parser_b = subparsers.add_parser("b", help="b parser help")
    parser_b.add_argument("-y", type=int, help="y help")

    args = parser.parse_args()


if __name__ == '__main__':
    main()