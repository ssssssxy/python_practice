#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import time
import logging
from random import randint


def run_time(timeout):
    """
    定义检查函数运行时间，并打印对应函数运行时间超出设定时间日志，并支持更改timeout
    """

    # 真正包裹函数
    print(timeout)
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            used_time = time.time() - start_time

            # 对于超出timeout的函数进行日志打印
            if used_time > timeout:
                print("-----", timeout)
                msg = '%s: %s > %s' % (func.__name__, used_time, timeout)
                logging.warning(msg)

            # python2
            # if used_time > timeout[0]:
            #   msg = '%s: %s > %s' % (func.__name__, used_time, timeout[0])
            #   logging.warn(msg)
            # return result

        # 设置timeout参数值
        def set_timeout(value):
            nonlocal timeout
            timeout = value

        wrapper.set_timeout = set_timeout

        # python2
        # def set_timeout(value):
        #   timeout[0] = value
        # wrapper.set_timeout = set_timeout

        return wrapper
    return out_wrapper

# @run_time(1.5)
# def func():
#     # 随机有50%的几率程序沉睡1秒
#     while randint(0, 1):
#         time.sleep(1)
#     print('func_run')


class a():
    def __init__(self, b):
        self.b = b

    b=1.5
    @run_time(b)
    def func(self):
        # 随机有50%的几率程序沉睡1秒
        while randint(0, 1):
            time.sleep(1)
        print('func_run')


if __name__ == "__main__":
    # 装饰器只能增强一次，修改b不生效
    d = a(3)
    print(d.b)
    print(a.b)
    a.b = 2
    d.func()

    # d = a(3)
    # print(d.b)
    # for _ in range(10):
    #     d.func()
    #
    # print('_' * 50)

    # 更改run_time装饰器中timeout参数
    # d.func.set_timeout(d.b)
    # for _ in range(10):
    #     d.func()