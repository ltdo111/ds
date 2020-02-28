#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/10 下午9:24
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : BSTset.py
# @Software: PyCharm
"""
from tree.BST.BST import BST


class BSTSet:
    def __init__(self):
        self.bst = BST()

    def get_size(self):
        return self.bst.get_size()

    def is_empty(self):
        return self.bst.is_empty()

    def add(self, e):
        self.bst.add(e)

    def contains(self, e):
        return self.contains(e)

    def remove(self, e):
        return self.remove(e)
