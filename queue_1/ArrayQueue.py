#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/4 下午4:58
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : queue.py
# @Software: PyCharm
# 队列 ， 底层同样使用动态数组
# 缺陷: 使用动态数组实现的队列，dequeue 时间复杂度是 O(n)
"""

from array.Array import Array


class ArrayQueue:
    def __init__(self, capacity=None):
        if capacity is None:
            self.array = Array()
        else:
            self.array = Array(capacity)

    def enqueue(self, val):
        """
        队尾入队
        :param val:
        :return:
        """
        self.array.add_last(val)

    def dequeue(self):
        """
        队首出队
        :return:
        """
        return self.array.remove_first()

    def get_front(self):
        return self.array.get_first()

    def get_size(self):
        return self.array.get_size()

    def is_empty(self):
        return self.array.is_empty()

    def to_string(self):
        res_queue_arr = []
        res_queue_arr.append('Queue: front [')
        for i in range(0, self.get_size()):
            val = self.array.get(i)
            if isinstance(val, int):
                val = str(val)
            res_queue_arr.append(val)
            if i != self.get_size() - 1:
                res_queue_arr.append(',')
        res_queue_arr.append('] tail')
        return "".join(res_queue_arr)


if __name__ == '__main__':
    arrayQueue = ArrayQueue()
    for i in range(0, 10):
        arrayQueue.enqueue(i)

    print(arrayQueue.to_string())

    arrayQueue.dequeue()
    print(arrayQueue.to_string())
    arrayQueue.enqueue(1)
    print(arrayQueue.to_string())
    arrayQueue.enqueue(12)
    print(arrayQueue.to_string())
