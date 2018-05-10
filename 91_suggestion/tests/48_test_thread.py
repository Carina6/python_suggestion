#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from time import sleep, ctime


# 48：使用 threading 模块编写多线程程序
def test_thread():
    print()

    def music(func):
        for i in range(2):
            print("I was listening to {}. {}".format(func, ctime()))
            sleep(5)  # 程序休眠 1 秒

    def move(func):
        for i in range(2):
            print("I was watching at the {}! {}".format(func, ctime()))
            sleep(1)

    threads = []
    t1 = threading.Thread(target=music, args=('爱情买卖',))
    threads.append(t1)
    t2 = threading.Thread(target=move, args=('阿凡达',))
    threads.append(t2)

    for t in threads:
        t.setDaemon(False)  # 声明线程为守护线程,true:表明主线程的退出可以不用等待子线程完成; false:所有的非守护线程结束后主线程才会结束
        t.start()
    t.join()  # 此方法能够阻塞当前上下文环境，直到调用该方法的线程终止或到达指定的 timeout
    # for 循环中的t 非循环中的局部变量，是test_thread方法中的局部变量
    print("all over {}".format(ctime()))