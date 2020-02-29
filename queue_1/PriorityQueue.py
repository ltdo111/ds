#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/28 下午10:00
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : PriorityQueue.py
# @Software: PyCharm
# 使用二叉大根堆实现一个优先队列
优先队列中的元素必须是具有可比较性的
"""
from heap.MaxHeap import MaxHeap


class PriorityQueue:
    def __init__(self):
        self.max_heap = MaxHeap()

    def enqueue(self, e):
        self.max_heap.add(e)

    def dequeue(self):
        self.max_heap.extra_max()

    def is_empty(self):
        return self.max_heap.is_empty()

    def get_size(self):
        return self.max_heap.get_size()

    def get_front(self):
        return self.max_heap.find_max()
