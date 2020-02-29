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
    def __init__(self, capacity=None, arr=None):
        if arr is not None:
            # 构建一个大根堆，通过heapify操作
            self._heapify(arr)
            return
        if capacity is None:
            self._data = Array()
        else:
            self._data = Array(capacity)

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
            raise (Exception, " index 0 doesn't have parent")
        return (index - 1) // 2  # 整形部分

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2

    def add(self, e):
        # 向堆中添加元素
        self._data.add_last(e)
        # 内部操作 Sift up(上浮，调整)
        self._sift_up(self.get_size() - 1)

    def _sift_up(self, index):
        while index > 0 and self._data.get(self._parent(index)) < self._data.get(index):
            # index > 0 并且当前最新加入的节点值大于其父亲节点的值
            self._data.swap(index, self._parent(index))
            index = self._parent(index)

    def find_max(self):
        if self._data.is_empty():
            raise (Exception, " can't find max when heap is empty!")
        return self._data.get_first()

    def _sift_down(self, index):
        """
        获取元素，下沉操作，核心是确定当前的节点有没有左右孩子,时间复杂度是log(n)
        :param index:
        :return:
        """
        while self._left_child(index) < self._data.get_size():
            comp_child_index = self._left_child(index)
            if comp_child_index + 1 < self._data.get_size() \
                    and self._data[comp_child_index + 1] > self._data[comp_child_index]:
                comp_child_index = self._right_child(index)
            if self._data[index] < self._data[comp_child_index]:
                # 如果当前索引下值 < 子树节点中最大的值，则交换位置
                self._data.swap(index, comp_child_index)
            else:
                break
            index = comp_child_index

    def extra_max(self):
        ret = self.find_max()
        self._data.swap(0, self._data.get_size() - 1)
        self._data.remove_last()
        # sift_down
        self._sift_down(0)  # 从根节点进行下浮

        return ret

    def replace(self, e):
        """
        替换堆顶元素、并调整堆，下沉操作
        :param e:
        :return:
        """
        ret = self.find_max()
        self._data.set(0, e)
        self._sift_down(0)
        return ret

    def _heapify(self, arr: Array):
        """
        将一个数组转化为二叉大根堆
        :param arr:
        :return:
        """
        self._data = arr
        for i in range(self._parent(arr.get_size() - 1), -1, -1):
            self._sift_down(i)


if __name__ == '__main__':
    print(3 // 2)
