#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/5 下午3:44
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : LinkedList.py
# @Software: PyCharm
# 自己实现链表元素需要的节点
# head 版
# 更新 新增tail节点，在链表头节点(head)进行新增和删除 操作复杂度都是 O(1)
# 在链表尾节点进行新增复杂度为O(1),但是删除还是O(n) 因为需要遍历链表得到被删除节点的prev节点
"""


class Node:
    def __init__(self, e=None, next=None):
        self.e = e
        self.next = next

    def to_string(self):
        return self.e


class LinkedList:
    """
    链表中的成员变量，head 指向链表中头节点，size 是链表中元素的个数
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, val):
        """
        头插法
        :param node:
        :return:
        """
        node = Node(e=val)
        node.next = self._head
        self._head = node
        # 简写
        # self._head = Node(val, self._head)
        self._size += 1

    def add(self, index, e):
        if index < 0 or index > self._size:
            raise (Exception, 'Add failed! Illegal index')
        if index == 0:
            # 这步操作可以通过虚拟头节点屏蔽掉
            self.add_first(e)
        else:
            prev = self._head
            for i in range(0, index - 1):
                prev = prev.next
            new_node = Node(e=e)
            new_node.next = prev.next
            prev.next = new_node
            # 简写
            prev.next = Node(e, prev.next)
        self._size += 1

    def add_last(self, e):
        self.add(self._size, e)


