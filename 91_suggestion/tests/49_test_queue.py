#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import urllib

import os
from queue import Queue

'''
Queue.Queue(maxsize)：先进先出，maxsize 为队列大小，其值为非正数的时候为无限循环队列
Queue.LifoQueue(maxsize)：后进先出，相当于栈
Queue.PriorityQueue(maxsize)：优先级队列

常用方法:
Queue.qsize()：返回近似的队列大小。当该值 > 0 的时候并不保证并发执行的时候 get() 方法不被阻塞，同样，对于 put() 方法有效。
Queue.empty()：队列为空的时候返回 True，否则返回 False
Queue.full()：当设定了队列大小的情况下，如果队列满则返回 True，否则返回 False
Queue.put(item[, block[, timeout]])：往队列中添加元素 item，block 设置为 False 的时候，如果队列满则抛出 Full 异常。
如果 block 设置为 True，timeout 为 None 的时候则会一直等待直到有空位置，否则会根据 timeout 的设定超时后抛出 Full 异常
Queue.put_nowait(item)：等于 put(item, False)
Queue.get([block[, timeout]])：从队列中删除元素并返回该元素的值
Queue.get_nowait()：等价于 get(False)
Queue.task_done()：发送信号表明出列任务已经完成，经常在消费者线程中用到
Queue.join()：阻塞直至队列中所有的元素处理完毕

Queue 中的队列和 collections.deque 所表示的队列并不一样，前者用于不同线程之间的通信，内部实现了线程的锁机制，后者是数据结构上的概念，支持 in 方法。
'''


# 49：使用 Queue 使多线程编程更加安全
# Queue实现了所需要的锁，是线程安全的
def test_queue():
    class DownloadThread(threading.Thread):

        def __init__(self, queue):
            threading.Thread.__init__(self)
            self.queue = queue

        def run(self):
            while True:
                url = self.queue.get()
                print('{0} begin download {1}...'.format(self.name, url))
                self.download_file(url)
                self.queue.task_done()  # 发送信号表明出列任务已经完成
                print('{0} download completed!!!'.format(self.name))

        def download_file(self, url):  # 下载网页源码
            urlhandler = urllib.request.urlopen(url)
            fname = os.path.basename(url) + '.html'
            with open(fname, 'wb') as f:
                while True:
                    chunk = urlhandler.read(1024)
                    if not chunk: break
                    f.write(chunk)

    urls = ['http://wiki.python.org/moin/WebProgramming',
            'https://wiki.python.org/moin/BeginnersGuide',
            'http://wiki.python.org/moin/Documentation'
            ]
    queue = Queue()

    for i in range(2):
        t = DownloadThread(queue)  # 多个线程共享queue队列
        t.setDaemon(True)
        t.start()

    for url in urls:
        queue.put(url)
    queue.join()