#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/6 下午2:09
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : LinkedListStack.py
# @Software: PyCharm
"""
from list.LinkedList_dummyHead import LinkedList


class LinkedListStack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, val):
        return self.list.add_first(val)

    def pop(self):
        return self.list.remove_first()

    def peek(self):
        return self.list.get_first()

    def is_empty(self):
        return self.list.is_empty()

    def get_size(self):
        return self.list.get_size()

    def to_string(self):
        res_linkedlist_arr = []
        res_linkedlist_arr.append(' LinkedListStack top [ ')
        res_linkedlist_arr.append(self.list.to_string())
        res_linkedlist_arr.append(' ] ')
        return "".join(res_linkedlist_arr)


if __name__ == '__main__':
    linkedListStack = LinkedListStack()
    for i in range(0, 5):
        linkedListStack.push(i)
        print(linkedListStack.to_string())

    linkedListStack.pop()
    print(linkedListStack.to_string())
