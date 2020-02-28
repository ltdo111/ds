#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/12 下午5:07
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : MaxHeap.py
# @Software: PyCharm
# 实现一个最大堆,使用动态(容量可变)数组去实现最大堆
"""

from array.Array import Array


class MaxHeap:
    def __init__(self, capacity=None):
        if capacity is None:
            self._data = Array()
        else:
            self._data = Array(capacity)

    def add(self, e):
        pass

    def get_size(self):
        return self._data.get_size()

    def is_empty(self):
        return self._data.is_empty()

    # 设置3个辅助函数, 通过给定节点的索引，计算当前节点的父亲索引、左孩子节点索引、右孩子节点索引
    def _parent(self, index):
        """
        返回完全二叉树的数组表示中，一个索引所表示的元素的父亲节点的索引
        :param index:
        :return:
        """
        if index == 0:
            raise (Exception, " index-0 doesn't have parent")
        return (index - 1) // 2

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2

    def add(self, e):
        ## 向堆中添加元素 + 内部操作 Sift up(上浮，调整)
        pass


if __name__ == '__main__':
    print(3 // 2)
