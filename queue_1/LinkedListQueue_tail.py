#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/6 下午8:42
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : LinkedListQueue_tail.py
# @Software: PyCharm
"""


class Node:
    def __init__(self, e=None, next=None):
        self.e = e
        self.next = next

    def to_string(self):
        return self.e


class LinkedListQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, val):
        """
        队尾插入
        :param val:
        :return:
        """
        if self._tail is None:
            self._tail = Node(e=val)
            self._head = self._tail
        else:
            self._tail.next = Node(e=val)
            self._tail = self._tail.next
        self._size += 1

    def dequeue(self):
        """
        队首删除
        :return:
        """
        if self.is_empty():
            raise (Exception, 'Dequeue failed！queue is empty!')
        del_node = self._head
        self._head = del_node.next
        del_node.next = None

        if self._head is None:
            """
            删除完元素后队列为空
            """
            self._tail = None

        self._size -= 1
        return del_node

    def is_empty(self):
        return self._size == 0

    def get_size(self):
        return self._size

    def get_front(self):
        if self.is_empty():
            raise (Exception, 'Get failed！queue is empty!')
        return self._head.e

    def to_string(self):
        res_linked_list_queue_arr = []
        res_linked_list_queue_arr.append(' LinkedListQueue: front [ ')
        cur = self._head
        while cur is not None:
            val = cur.e
            if isinstance(val, int):
                val = str(val)

            res_linked_list_queue_arr.append(val + '->')
            cur = cur.next
        res_linked_list_queue_arr.append('None ] tail')
        return "".join(res_linked_list_queue_arr)


if __name__ == '__main__':
    linkedListQueue = LinkedListQueue()
    for i in range(0, 10):
        linkedListQueue.enqueue(val=i)
        print(linkedListQueue.to_string())

    linkedListQueue.dequeue()
    print(linkedListQueue.to_string())

    print(linkedListQueue.is_empty())

    print(linkedListQueue.get_size())

    print(linkedListQueue.get_front())

    linkedListQueue.enqueue(10)
    print(linkedListQueue.to_string())
    print(linkedListQueue.get_size())