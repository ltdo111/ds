#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/5 下午3:44
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : LinkedList.py
# @Software: PyCharm
# 自己实现链表元素需要的节点
# dummy_head(虚拟头节点)版
# 删除和新增都需要找到前一个节点
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
        self._dummy_head = Node(None, None)
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, index, e):
        """
        实质是占用原有index元素的位置，并将原有index元素向后移动
        :param index:
        :param e:
        :return:
        """
        if index < 0 or index > self._size:
            raise (Exception, 'Add failed! Illegal index')

        prev = self._dummy_head
        for i in range(0, index):
            prev = prev.next
        new_node = Node(e=e)
        new_node.next = prev.next
        prev.next = new_node
        # 简写
        # prev.next = Node(e, prev.next)
        self._size += 1

    def add_first(self, e):
        """
        头插法
        :param e:
        :return:
        """
        self.add(0, e)

    def add_last(self, e):
        self.add(self._size, e)

    def get(self, index):
        if index < 0 or index > self._size:
            raise (Exception, 'Get failed! Illegal index')
        # 链表的真实头节点
        cur = self._dummy_head.next
        for i in range(0, index):
            cur = cur.next
        return cur.e

    def get_first(self):
        return self.get(0)

    def get_last(self):
        return self.get(self._size - 1)

    # 更新操作
    def set(self, index, e):
        if index < 0 or index > self._size:
            raise (Exception, 'set failed! Illegal index')
        cur = self._dummy_head.next
        for i in range(0, index):
            cur = cur.next
        cur.e = e

    # 删除操作
    def remove(self, index):
        if index < 0 or index > self._size:
            raise (Exception, 'set failed! Illegal index')
        prev = self._dummy_head
        for i in range(0, index):
            prev = prev.next
        del_node = prev.next
        prev.next = del_node.next
        del_node.next = None
        self._size -= 1
        return del_node.e

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def remove_element(self, e):
        prev = self._dummy_head
        while prev.next is not None:
            if prev.next.e == e:
                break
            prev = prev.next

        if prev.next is not None:
            del_node = prev.next
            prev.next = del_node.next
            del_node.next = None

    # 查找链表中是否存在某个元素
    def contains(self, e):
        cur = self._dummy_head.next
        while cur is not None:
            if cur.e == e:
                return True
            cur = cur.next
        return False

    def to_string(self):
        res_linkedlist_arr = []
        res_linkedlist_arr.append('LinkedList:size = %d  ' % self._size)
        cur = self._dummy_head.next
        while cur is not None:
            val = cur.e
            if isinstance(val, int):
                val = str(val)
            res_linkedlist_arr.append(val + ' -> ')
            cur = cur.next
        res_linkedlist_arr.append(' NULL ')
        return "".join(res_linkedlist_arr)


if __name__ == '__main__':
    a = 1
    linkedList = LinkedList()
    for i in range(0, 5):
        linkedList.add_first(i)
        print(linkedList.to_string())

    linkedList.set(0, 2)
    print(linkedList.to_string())
    linkedList.add(5, 10)
    print(linkedList.to_string())

    linkedList.remove_first()
    print(linkedList.to_string())

    linkedList.remove_last()
    print(linkedList.to_string())

    linkedList.remove(1)
    print(linkedList.to_string())
