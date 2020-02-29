#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/29 上午10:42
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : AVLTree.py
# @Software: PyCharm
# 实现平衡二叉树 AVLTree
# AVL 树对每一个节点来说，其左右子树的高度差不超过1， 即平衡因子不超过1
# 比BST 多了自平衡机制，记录每个节点的高度，以及平衡因子
# 章节:
   1.  AVL 定义 每个节点的左右子树的高度差不超过1
   2.  每个节点定义其高度、和平衡因子
   3.  先检查确保是二分搜索树、再检查是否平衡 check
   4.  AVL 通过左旋 右旋实现平衡 以及基本原理 以及什么时候进行自平衡操作
       LL(左孩子的左侧新加入一个节点) RR (右孩子的右侧新加入一个节点)
       LR(左孩子的右侧新加入一个节点) RL (有孩子的左侧新加入一个节点)
   5.
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
        # 每个节点的初始高度为1
        self.height = 1


class AVLTree:
    def __init__(self, root: Node = None):
        self._root = root
        self._size = 0

    def get_size(self):
        return self._size

    def _get_height(self, node: Node):
        if node is None:
            return 0
        return node.height

    def _get_balance_factor(self, node: Node):
        """
        计算每个节点的平衡因子
        :param node:
        :return:
        """
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def is_bst(self):
        """
        当前这棵树是否是一个二分搜索树
        二分搜索树的中序遍历结果
        :return:
        """
        keys = []
        self._in_order(self._root, keys)
        for i, key in enumerate(keys, 1):
            if keys[i - 1] > key:
                return False
        return True

    def _right_rotate(self, y: Node):
        """
        因为左边子树发生偏移，所以执行右旋操作
        :param y:
        :return:
               y                       x
              / \                     /  \
             x   T4 ---> 向右旋转     z     y
            / \                    / \    / \
           z   T3                 T1  T2  T3 T4
          / \
         T1  T2
        """
        x = y.left
        T3 = x.right
        x.right = y
        y.left = T3

        # 更新height 的值
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        return x

    def _left_rotate(self, y: Node):
        """
        因为右子树发生偏移，所以执行左旋操作
        :param y:
        :return:
             y                             x
            / \                          /   \
           T1  x                        y     z
              / \     ----> 向左旋转     / \   / \
            T2   z                     T1 T2 T3 T4
                / \
               T3 T4
        """
        x = y.right
        T2 = x.left
        x.right = y
        y.left = T2

        # 更新高度 height 的值
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1

    def _is_balanced(self, node: Node):
        """
        递归来验证当前树是否是一棵平衡二叉树
        :param node:
        :return:
        """
        if node is None:
            return True
        balance_factory = self._get_balance_factor(node)
        if abs(balance_factory) > 1:
            """当前这个节点的平衡因子是否满足平衡二叉树的定义"""
            return False
        # 当前这个节点的左右子树是否满足平衡二叉树的定义
        return self._is_balanced(node.left) and self._is_balanced(node.right)

    def is_balanced(self):
        """
        递归判断每个节点上的平衡因子是否<=1
        :return:
        """
        return self._is_balanced(self._root)

    def _in_order(self, node: Node, keys):
        if node is None:
            return
        self._in_order(node.left, keys)
        keys.append(node.key)
        self._in_order(node.right, keys)

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

    def _add_element(self, node, key, val):
        """
        递归构建二分搜索树
        :param node:
        :param key:
        :param val:
        :return:
        """
        if node is None:
            self._size += 1
            """
            返回的是子树根节点
            """
            return Node(key, val)
        elif key < node.key:
            node.left = self._add_element(node.left, key, val)
        elif key > node.key:
            # insert
            node.right = self._add_element(node.right, key, val)
        else:
            # or update
            node.val = val

        # 更新节点高度 - height ,递归的巧妙之处，一次节点插入为将所有的-all节点高度进行更新
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        # 更新节点平衡因子
        balance_factory = self._get_balance_factor(node)
        if abs(balance_factory) > 1:
            """
            添加新元素后这个节点的平衡因子>1 此时二叉树不是平衡二叉树 AVL 树
            """
            print("unbalanced: ", + balance_factory)

        # 平衡维护
        if balance_factory > 1 and self._get_balance_factor(node.left) >= 0:
            """不平衡场景，该节点左侧的左侧还是节点, 整体向左偏斜"""
            # 右旋转操作
            return self._right_rotate(node)
        if balance_factory < -1 and self._get_balance_factor(node.right) <= 0:
            """不平衡场景，该节点右侧的右侧还是节点，整体向右偏斜"""
            return self._left_rotate(node)

        return node


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
