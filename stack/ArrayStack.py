#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/1/18 下午7:21
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : Stack.py
# @Software: PyCharm
"""
from array.Array import Array


class ArrayStack:
    def __init__(self, capacity=None):
        """
        :param capacity: 栈的容积
        """
        if capacity is None:
            self.array = Array()
        else:
            self.array = Array(capacity)

    def push(self, val):
        """
        向数组的末尾添加一个元素
        :param val:
        :return:
        """
        self.array.add_last(val)

    def pop(self):
        """
        弹出栈顶的元素，其实是栈顶的元素, 并删除
        :return:
        """
        return self.array.remove_last()

    def peek(self):
        """
        获取栈顶的元素，其实是数组的末尾元素
        :return:
        """
        return self.array.get_last()

    def get_size(self):
        return self.array.get_size()

    def is_empty(self):
        return self.array.is_empty()

    def get_capacity(self):
        return self.array.get_capacity()

    def to_string(self):
        res_str_stack = []
        res_str_stack.append('Stack: [')
        for i in range(0, self.array.get_size()):
            val = self.array.get(i)
            if isinstance(val, int):
                val = str(val)
            res_str_stack.append(val)
            if i != self.array.get_size() - 1:
                res_str_stack.append(',')
        res_str_stack.append('] top')
        return "".join(res_str_stack)


if __name__ == '__main__':
    # 1. 构建一个栈
    stack = ArrayStack(10)
    for i in range(0, 5):
        stack.push(i)
        print(stack.to_string())

    stack.pop()
    print(stack.to_string())
