#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/7 下午3:56
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : Delete_Solution_recursion.py
# @Software: PyCharm
"""


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        pass

    def remove_elements(self, head: ListNode, val):
        if head is None:
            """
            没有元素可以删除
            """
            return head

        # 递归删除后续元素
        res = self.remove_elements(head.next, val)
        if head.val == val:
            """
            头节点判定为需要被删除的元素 - 事实上目标元素都是从这里删除的
            """
            return res
        else:
            """
             头节点不被删除
            """
            head.next = res
            return head
