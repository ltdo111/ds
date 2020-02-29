#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/11 上午11:01
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : BSTMap.py
# @Software: PyCharm
"""


class Node:
    """
    定义了key->val 键值对
    """
    def __init__(self, key=None, val=None, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class BSTMap:
    def __init__(self, root: Node = None):
        self._root = root
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def contains(self, key):
        return self._get_node(self._root, key) is not None

    def _get_node(self, node, key):
        """
        递归获取 key 对应的 node
        :param node:
        :param key:
        :return:
        """
        if node is None:
            return None

        if node.key == key:
            return node

        if key < node.key:
            return self._get_node(node.left, key)
        if key > node.key:
            return self._get_node(node.right, key)

    def add(self, key, val):
        self._root = self._add_element(self._root, key, val)

    def _add_element(self, root, key, val):
        """
        递归构建二分搜索树
        :param root:
        :param e:
        :return:
        """
        if root is None:
            self._size += 1
            """
            返回的是子树根节点
            """
            return Node(key, val)
        elif key < root.key:
            root.left = self._add_element(root.left, key, val)
        elif key > root.key:
            # insert
            root.right = self._add_element(root.right, key, val)
        else:
            # or update
            root.val = val
        return root

    def get(self, key):
        node = self._get_node(self._root, key)
        if node is None:
            return None
        return node.val

    def set(self, key, new_val):
        node = self._get_node(self._root, key)
        if node is None:
            raise (Exception, key + " doesn't exist!")
        node.val = new_val

    def _minimum(self, node: Node):
        """
        递归-找到二分搜索树中最小元素
        :param node:
        :return:
        """
        if node.left is None:
            return node
        return self._minimum(node.left)

    def _remove_minimum(self, node: Node):
        """
        删除二分搜索树中的最小节点，返回删除节点后新的二分搜索树的根
        :param node:
        :return:
        """
        if node.left is None:
            # 此刻已经遍历到底，当前node为已经遍历到的值
            right_node = node.right
            node.right = None
            self._size -= 1
            return right_node
        node.left = self._remove_minimum(node.left)
        return node

    def remove(self, key):
        """
        从bst 中删除元素为key的节点
        :param key:
        :return:
        """
        node = self._get_node(self._root, key)
        if node is not None:
            self._root = self._remove(self._root, key)
            return node.val
        return None

    def _remove(self, node: Node, key):
        """
        删除以node为根的BST 中节点为e的节点，递归算法
        返回删除节点后新的二分搜索树中的根
        :param node:
        :param key:
        :return:
        """
        if node is None:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
            return node
        elif key > node.key:
            node.right = self._remove(node.right, key)
            return node
        else:  # key == node.key
            if node.left is None:
                right_node = node.right
                node.right = None
                self._size -= 1
                return right_node
            if node.right is None:
                left_node = node.left
                node.left = None
                self._size -= 1
                return left_node

            del_node = node
            # 找到后继节点,当前被删除的右子树的最小元素
            next_node = self._minimum(del_node.right)
            next_node.right = self._remove_minimum(del_node.right)
            next_node.left = del_node.left
            del_node.left = del_node.right = None
            return next_node
