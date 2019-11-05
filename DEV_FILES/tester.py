#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time
from concurrent import futures

def task (n):
    print('{}: sleeping'.format(n))
    time.sleep(5)
    print('{}: done'.format(n))
    return n / 10

def done (fn):
    if fn.cancelled():
        print('{}: canceled'.format(fn.arg))
    elif fn.done():
        error = fn.exception()
        if error:
            print('{}: error returned {}'.format(fn.arg, error))
        else:
            result = fn.result()
            print('{}: value returned: {}'.format(fn.arg, result))

def sth (x):
    print("Yeah it works")


t1 = futures.ThreadPoolExecutor(max_workers=2)
print('main starting')
f = t1.submit(task, 5)
f.arg = 5
print("bef call")
f.add_done_callback(sth)
print('af call')
#result = f.result()
#print('Yup?')
