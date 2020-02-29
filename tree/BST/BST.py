#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/2/8 下午12:48
# @Author  : bofengliu@tencent.com
# @Site    : 
# @File    : BST.py
# @Software: PyCharm
# 二分搜索树 不会存储相同的元素
"""
from stack.LinkedListStack import LinkedListStack
from queue_1.LinkedListQueue_tail import LinkedListQueue


class Node:
    def __init__(self, e=None, left=None, right=None):
        self.e = e
        self.left = left
        self.right = right


class BST:
    def __init__(self, root: Node = None):
        """
        根节点
        :param root:
        """
        self._root = root
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, e):
        self._root = self._add_element(self._root, e)

    def _add_element(self, root, e):
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
            return Node(e)
        elif e < root.e:
            root.left = self._add_element(root.left, e)
        elif e > root.e:
            root.right = self._add_element(root.right, e)
        return root

    def add_v0(self, e):
        """
        递归实现向BST中添加元素
        :param e:
        :return:
        """
        if self._root is None:
            root_node = Node(e, None, None)
            self._root = root_node
            self._size += 1
        else:
            self._add_element_v0(self._root, e)

    def _add_element_v0(self, root, e):
        """
        向一个root节点为根节点的BTS添加元素
        :param root:
        :param e:
        :return:
        """
        if root.e == e:
            return
        elif e < root.e and root.left is None:
            root.left = Node(e, None, None)
            self._size += 1
            return
        elif e > root.e and root.right is None:
            root.right = Node(e, None, None)
            self._size += 1
            return
        if e < root.e:
            self._add_element(root.left, e)
        else:
            self._add_element(root.right, e)

    def contains(self, e):
        return self._contains(self._root, e)

    def _contains(self, node, e):
        if node is None:
            return False

        if node.e == e:
            return True

        if e < node.e:
            return self._contains(node.left, e)
        if e > node.e:
            return self._contains(node.right, e)

    def pre_order(self):
        """
        前序遍历
        :return: 
        """
        self._pre_order(self._root)

    def _pre_order(self, node):
        if node is None:
            return

        print(node.e)

        self._pre_order(node.left)
        self._pre_order(node.right)

    def pre_order_nr(self):
        """
        前序遍历-非递归，使用栈 DFS 深度优先遍历
        :return:
        """
        stack = LinkedListStack()
        stack.push(self._root)
        while stack.is_empty() is False:
            cur = stack.pop()
            print(cur.e)
            if cur.right is not None:
                stack.push(cur.right)
            if cur.left is not None:
                stack.push(cur.left)

    def level_order(self):
        """
        队列实现中序遍历 - 先进先出
        :return:
        """
        queue = LinkedListQueue()
        queue.enqueue(self._root)
        while queue.is_empty() is False:
            cur = queue.dequeue()
            print(cur.e.e)
            if cur.e.left is not None:
                queue.enqueue(cur.e.left)
            if cur.e.right is not None:
                queue.enqueue(cur.e.right)

    def in_order(self):
        """
        中序遍历，即是二分搜索树从小到大排序的数据
        :return:
        """
        self._in_order(self._root)

    def _in_order(self, node):
        if node is None:
            return

        self._in_order(node.left)
        print(node.e)
        self._in_order(node.right)

    def post_order(self):
        """
        后续遍历
        :return:
        """
        self._post_order(self._root)

    def _post_order(self, node):
        if node is None:
            return
        self._post_order(node.left)
        self._post_order(node.right)
        print(node.e)

    def minimum_nr(self):
        if self._root is None:
            return None
        else:
            cur = self._root
            while cur.left is not None:
                cur = cur.left
            return cur.e

    def minimum(self):
        if self._size == 0:
            raise (Exception, 'BST is empty')
        return self._minimum(self._root)

    def _minimum(self, node: Node):
        """
        递归-找到二分搜索树中最小元素
        :param node:
        :return:
        """
        if node.left is None:
            return node
        return self._minimum(node.left)

    def maximum(self):
        if self._size == 0:
            raise (Exception, 'BST is empty')
        return self._maximum(self._root).e

    def _maximum(self, node: Node):
        """
        递归-找到二分搜索树中最大元素
        :param node:
        :return:
        """
        if node.right is None:
            return node
        return self._maximum(node.right)

    def maximum_nr(self):
        if self._root is None:
            return None
        else:
            cur = self._root
            while cur.right is not None:
                cur = cur.right
            return cur.e

    def remove_minimum(self):
        ret = self.minimum()
        self._root = self._remove_minimum(self._root)
        return ret

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

    def remove_maximum(self):
        ret = self.maximum()
        self._root = self._remove_maximum(self._root)
        return ret

    def _remove_maximum(self, node: Node):
        if node.right is None:
            left_node = node.left
            node.left = None
            self._size -= 1
            return left_node
        node.right = self._remove_maximum(node.right)
        return node

    def remove(self, e):
        """
        从bst 中删除元素为e的节点
        :param e:
        :return:
        """
        self._root = self._remove(self._root, e)

    def _remove(self, node: Node, e):
        """
        删除以node为根的BST 中节点为e的节点，递归算法
        返回删除节点后新的二分搜索树中的根
        :param node:
        :param e:
        :return:
        """
        if node is None:
            return None
        if e < node.e:
            node.left = self._remove(node.left, e)
            return node
        elif e > node.e:
            node.right = self._remove(node.right, e)
            return node
        else:  # e == node.e
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

    def to_string(self):
        res_bst_arr = []
        res_bst_arr.append('BST: \n')
        self._generate_bst_str(self._root, 0, res_bst_arr)
        return "".join(res_bst_arr)

    def _generate_bst_str(self, root, depth, res_bst_arr):
        if root is None:
            res_bst_arr.append(self.generate_depth_str(depth) + 'Null\n')
            return
        val = root.e
        if isinstance(val, int):
            val = str(val)
        res_bst_arr.append(self.generate_depth_str(depth) + val + "\n")
        self._generate_bst_str(root.left, depth + 1, res_bst_arr)
        self._generate_bst_str(root.right, depth + 1, res_bst_arr)

    def generate_depth_str(self, depth):
        depth_str_arr = []
        for i in range(0, depth):
            depth_str_arr.append('--')
        return "".join(depth_str_arr)


if __name__ == '__main__':
    bst = BST()
    arr = [5, 3, 2, 4, 6, 8]
    for i, val in enumerate(arr):
        bst.add(val)
    # 根节点在最先
    # bst.pre_order()
    # bst.pre_order_nr()
    # # 根节点在中间，且元素从小到大依次排开
    # bst.in_order()
    # # 根节点在最后
    # bst.post_order()
    # bst.level_order()
    # print(bst.minimum_nr())
    # print(bst.maximum_nr())

    # bst.remove_maximum()
    # print(bst.to_string())
    bst.remove_minimum()
    print(bst.to_string())
