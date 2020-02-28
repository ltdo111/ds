#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/1/18 下午7:36
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : Array.py
# @Software: PyCharm
# 动态数组
"""


class Array:
    def __init__(self, capacity=None):
        """
        包含无餐和有参两种情况
        :param capacity:
        """
        if capacity is None:
            # self.data = []
            self._data = [0] * 10
        else:
            self._data = [0] * capacity
        self._size = 0

    def get_size(self):
        """
        当前结构中已存储的元素的个数
        :return:
        """
        return self._size

    def get_capacity(self):
        return len(self._data)

    def is_empty(self):
        return self._size == 0

    def add_first(self, val):
        self.add(0, val)

    def add_last(self, val):
        self.add(self._size, val)

    def add(self, index, val):
        """
        向数组指定位置插入val
        :param index:
        :param val:
        :return:
        """
        if index < 0 or index > self._size:
            raise (Exception, 'AddList failed. require index >=0 and index <= size')

        if self._size == len(self._data):
            # 已有元素的个数 == 数组的capacity, java 中arrayList 的扩充因子是1.5
            self._resize(2 * len(self._data))

        # 目标位置元素向后移动
        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]

        self._data[index] = val
        self._size += 1

    def _resize(self, new_capacity):
        new_data = [None] * int(new_capacity)
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data

    def to_string(self):
        res_str_arr = []
        res_str_arr.append('Array: size = %d, capacity = %d; ' % (self._size, len(self._data)))
        for i in range(0, self._size):
            val = self._data[i]
            if isinstance(val, int):
                val = str(val)
            res_str_arr.append(val)
            if i != self._size - 1:
                res_str_arr.append(',')
        res_str_arr.append(']')
        return "".join(res_str_arr)

    def get(self, index):
        """
        保证数据安全，用户无法知晓整个数组的详情
        :param index:
        :return:
        """
        if index < 0 or index > self._size:
            raise ValueError('index beyond arr size or index under 0, size is %d' % self._size)
        return self._data[index]

    def get_last(self):
        self.get(self._size - 1)

    def get_first(self):
        self.get(0)

    def set(self, index, val):
        if index < 0 or index > self._size:
            raise ValueError('index beyond arr size or index under 0, size is %d' % self._size)
        self._data[index] = val

    def contains(self, val):
        for i in range(self._size):
            if self._data[i] == val:
                return True
        return False

    def find(self, val):
        for i in range(self._size):
            if self._data[i] == val:
                return i
        return -1

    def remove(self, index):
        """
        从数组中删除某一位置的元素，并返回被删除的元素
        :param index:
        :return:
        """
        if index < 0 or index >= self._size:
            raise ValueError('index beyond arr size or index under 0, size is %d' % self._size)

        ret = self._data[index]

        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        self._data[self._size] = None

        if self._size == len(self._data) / 2:
            self._resize(len(self._data) / 2)

        return ret

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def remove_element(self, val):
        """
        find数组中第一次出现的元素，并删除
        :param val:
        :return:
        删除一个元素: 先找 后 删除
        """
        index = self.find(val)
        if index != -1:
            self.remove(index)


if __name__ == '__main__':
    # new 自己的Array 类
    arr = Array(2)

    for i in range(0, 1):
        arr.add_last(i)

    print(arr.to_string())

    arr.add(1, 666)
    print(arr.to_string())

    arr.add_first(-1)
    print(arr.to_string())

    arr.remove_first()
    # print(arr.get(0))
    print(arr.to_string())
    #
    # arr.remove(1)
    # print(arr.to_string())
    #
    # arr.remove(2)
    # print(arr.to_string())
    #
    # arr.remove_first()
    # print(arr.to_string())
    #
    # arr.remove_last()
    # print(arr.to_string())
