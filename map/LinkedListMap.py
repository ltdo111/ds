#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/11 上午11:01
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : LinkedListMap.py
# @Software: PyCharm
"""


class Node:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next

    def to_string(self):
        return self.key + ' : ' + self.val


class LinkedListMap:
    def __init__(self):
        self._dummy_head = Node(None, None, None)
        self._size = 0

    def add(self, key, val):
        node = self._get_node(key)
        if node is None:
            self._dummy_head.next = Node(key, val, self._dummy_head.next)
            self._size += 1
        else:
            node.val = val

    def remove(self, key):
        prev = self._dummy_head
        while prev.next is not None:
            if prev.next.key == key:
                break
            prev = prev.next

        if prev.next is not None:
            del_node = prev.next
            prev.next = del_node.next
            del_node.next = None
            self._size -= 1
            return del_node.val
        return None

    def contains(self, key):
        return self._get_node(key) is not None

    def get(self, key):
        node = self._get_node(key)
        if node is not None:
            return node.val
        return None

    def set(self, key, new_val):
        node = self._get_node(key)
        if node is None:
            raise (Exception, key + " doesn't exist!")
        node.val = new_val

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _get_node(self, key):
        cur = self._dummy_head.next
        while cur is not None:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

