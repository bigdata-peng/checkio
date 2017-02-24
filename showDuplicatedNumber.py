#!/usr/bin/env python
# encoding: utf-8


"""
@author: bigdata
@file: showDuplicatedNumber.py
@time: 24/2/17 11:01 AM
"""

# Input: A list of integers.
#
# Output: The list of integers.
#
# Example:
#
# checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
# checkio([1, 2, 3, 4, 5]) == []
# checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
# checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]


import collections
import time

## Evaluate the time

_start_time = time.time()

def tic():
    global _start_time
    _start_time = time.time()

def tac():
    t_sec = round(time.time() - _start_time)
    (t_min, t_sec) = divmod(t_sec,60)
    (t_hour,t_min) = divmod(t_min,60)
    print('Time passed: {}hour:{}min:{}sec'.format(t_hour,t_min,t_sec))

def checkio(a):
    dup =  [item for item, count in collections.Counter(a).items() if count > 1]
    results = [x for x in a if x in dup]
    return results


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    tic()
    print checkio([1, 2, 3, 1, 3])
    print checkio([1, 2, 3, 4, 5])
    print checkio([5, 5, 5, 5, 5])
    print checkio([10, 9, 10, 10, 9, 8])
    tac()