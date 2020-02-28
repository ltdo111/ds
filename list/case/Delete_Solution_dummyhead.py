#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/7 下午1:46
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : Delete_Solution_dummyhead.py
# @Software: PyCharm
"""


class ListNode:
    def __init__(self, e=None, next=None):
        self.val = e
        self.next = next


class Solution:
    def __init__(self):
        pass

    def remove_elements(self, head: ListNode, val):
        dummy_head = ListNode(None, head)

        # 删除中间的元素, 此时head 肯定不是要删除的元素了
        prev = dummy_head
        while prev.next is not None:
            if prev.next.val == val:
                del_node = prev.next
                prev.next = del_node.next
                del_node.next = None
            else:
                prev = prev.next

        return dummy_head.next
