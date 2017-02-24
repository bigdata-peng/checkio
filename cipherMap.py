#!/usr/bin/env python
# encoding: utf-8


"""
@author: bigdata
@license: Apache Licence 
@file: cipherMap.py
@time: 24/2/17 12:52 PM
"""
import time
import numpy as np


_start_time = time.time()
CODE_LENGTH = 4


def tic():
    global _start_time
    _start_time = time.time()


def tac():
    t_sec = round(time.time() - _start_time)
    (t_min, t_sec) = divmod(t_sec, 60)
    (t_hour, t_min) = divmod(t_min, 60)
    print('Time passed: {}hour:{}min:{}sec'.format(t_hour, t_min, t_sec))


def recall_password(pattern, codemap):

    ## Convert tuple into array
    ptn = [list (i) for i in pattern]
    ptn = np.array(ptn)
    cm = [list (i) for i in codemap]
    cm = np.array(cm)
    location = (ptn == "X")

    str = []

    for i in range(0, CODE_LENGTH):
        partialCode = cm[location]
        str.append(partialCode.tolist())
        location = np.rot90(location, k=3)

    results = "".join((reduce(lambda x, y: x + y, str)))
    return results

class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    tic()
    print recall_password( \
        ('X...', \
         '..X.', \
         'X..X', \
         '....'), \
        ('itdf', \
         'gdce', \
         'aton', \
         'qrdi'))

    print recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr'))

    tac()
