#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import os
import time
import multiprocessing

QUEUE = multiprocessing.Manager().Queue()

def task():
    print('父进程:', os.getpid())
    time.sleep(20)

if __name__ == "__main__":
    print('0 父进程:', os.getpid())
    number = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(number)
    for i in range(number):
        pool.apply_async(task)
    pool.close()
    pool.join()
