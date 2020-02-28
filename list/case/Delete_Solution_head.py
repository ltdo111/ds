#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/7 下午12:41
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : Delete_Solution.py
# @Software: PyCharm
# leetcode 删除链表中元素
"""


class ListNode:
    def __init__(self, e=None, next=None):
        self.val = e
        self.next = next


class Solution:
    def __init__(self):
        pass

    def remove_elements(self, head: ListNode, val):
        while head is not None and head.val == val:
            del_node = head
            head = head.next
            del_node.next = None

        if head is None:
            return head

        # 删除中间的元素, 此时head 肯定不是要删除的元素了
        prev = head
        while prev.next is not None:
            if prev.next.val == val:
                del_node = prev.next
                prev.next = del_node.next
                del_node.next = None
            else:
                prev = prev.next

        return head
