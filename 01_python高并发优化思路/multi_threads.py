#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
import threading

QUEUE = list()

def fibonacci(n):
    '''斐波拉数列'''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def init_queue():
    '''初始化队列'''
    global QUEUE
    QUEUE = list(range(10))[::-1]

def task():
    while len(QUEUE) != 0:
        try:
            data = QUEUE.pop()
            print('work', data, 'start', end=' -> ')
            fibonacci(34)
            print('end')
        except Exception as ex:
            print(str(ex))

if __name__ == "__main__":
    print('单线程测试开始')
    init_queue()
    start_time = time.time()
    th = threading.Thread(target=task)
    th.start()
    th.join()
    single_time = time.time() - start_time

    print('\n多线程测试开始')
    init_queue()
    start_time = time.time()

    thread_list = list()
    for i in range(4):
        th = threading.Thread(target=task)
        th.start()
        thread_list.append(th)

    for t in thread_list:
        t.join()

    multi_time = time.time() - start_time

    print("单线程执行：", single_time)
    print("多进程执行：", multi_time)
