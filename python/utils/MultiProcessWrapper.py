#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 11:01 下午
# @Author  : archchen
# @Description   : 多进程装饰器
import os
import multiprocessing
import time
from threading import Thread


def multi(func):
    def threadWarp(target, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        process = multiprocessing.Process(target=target, args=args, kwargs=kwargs)
        process.start()
        process.join()

    def inner(*args, **kwargs):
        Thread(target=threadWarp, args=(func, args, kwargs)).start()

    return inner


@multi
def worker(i, name):
    print(name)
    print(name, 'Starting')
    print(fib(i))
    print(name, 'ending')


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    for i in range(40, 60):
        worker(i, 'worker:' + str(i))
