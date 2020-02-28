#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/4 下午3:29
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : Solution.py
# @Software: PyCharm
"""

from stack.Stack import Stack


class Solution:
    def __init__(self):
        pass

    def is_valid(self, s):
        array_stack = Stack()
        str_list = list(s)
        for index, char in enumerate(str_list):
            if char == '(' or char == '{' or char == '[':
                array_stack.push(char)
            else:
                if array_stack.is_empty():
                    return False

                top_char = array_stack.pop()
                if char == ')' and top_char != '(':
                    return False
                if char == ']' and top_char != '[':
                    return False
                if char == '}' and top_char != '{':
                    return False

        return array_stack.is_empty()


if __name__ == '__main__':
    solution = Solution()
    valid_str = '}[['
    print(solution.is_valid(valid_str))

    valid_str = '{}'
    print(solution.is_valid(valid_str))

    valid_str = '{[]}'
    print(solution.is_valid(valid_str))
