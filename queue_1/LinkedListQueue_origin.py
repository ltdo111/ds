#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/6 下午2:52
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : LinkedListQueue.py
# @Software: PyCharm
"""
from list.LinkedList_dummyHead import LinkedList


class LinkedListQueue:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, val):
        self.list.add_first(val)

    def dequeue(self):
        return self.list.remove_last()

    def get_front(self):
        return self.list.get_last()

    def get_size(self):
        return self.list.get_size()

    def is_empty(self):
        return self.list.is_empty()

    def to_string(self):
        res_linkedList_queue_arr = []
        res_linkedList_queue_arr.append(' linkedListQueen: tail [')
        res_linkedList_queue_arr.append(self.list.to_string())
        res_linkedList_queue_arr.append(' ] front')
        return "".join(res_linkedList_queue_arr)


if __name__ == '__main__':
    linkedListQueue = LinkedListQueue()
    for i in range(0, 10):
        linkedListQueue.enqueue(i)
        print(linkedListQueue.to_string())

    linkedListQueue.dequeue()
    print(linkedListQueue.to_string())
