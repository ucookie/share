#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import time
import gevent

def task0():
    print("Task0 begin")
    gevent.sleep(5)
    print("Task0 end")

def task1():
    print("Task1 begin")
    gevent.sleep(3)
    print("Task1 end")

def task2():
    print("Task2 begin")
    gevent.sleep(0)
    print("Task2 end")

if __name__ == "__main__":
    print('串行测试')
    start_time = time.time()
    task0()
    task1()
    task2()
    single_time = time.time() - start_time

    print('\n协程测试')
    start_time = time.time()
    gevent.joinall([
        gevent.spawn(task0),
        gevent.spawn(task1),
        gevent.spawn(task2),
    ])
    multi_time = time.time() - start_time

    print("串行测试：", single_time)
    print("协程测试：", multi_time)
