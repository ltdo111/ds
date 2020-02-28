#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/10 下午9:54
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : LinkedListSet.py
# @Software: PyCharm
"""
from list.LinkedList_dummyHead import LinkedList


class LinkedListSet:
    def __init__(self):
        self._linkedList = LinkedList()

    def get_size(self):
        return self._linkedList.get_size()

    def is_empty(self):
        return self._linkedList.is_empty()

    def contains(self, e):
        return self._linkedList.contains(e)

    def add(self, e):
        if self._linkedList.contains(e) is False:
            # O(1) 复杂度
            self._linkedList.add_first(e)

    def remove(self, e):
        self._linkedList.remove_element(e)
