#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/7 下午2:37
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : Sum.py
# @Software: PyCharm
"""


class Sum:
    def __init__(self):
        pass

    def sum(self, arr):
        return self._cal_sum(arr, 0)

    def _cal_sum(self, arr, left):
        if left == len(arr):
            return 0
        return arr[left] + self._cal_sum(arr, left + 1)


if __name__ == '__main__':
    arr = [1, 2, 3]

    print(Sum().sum(arr))
