#!/usr/bin/env python
# https://leetcode.cn/problems/maximum-binary-tree/
from __future__ import annotations

import unittest
from typing import Optional, List

from leetcode.sort_list import TreeNode


class MaximumBinaryTreeNode(TreeNode):
    @staticmethod
    def construct_maximum_binary_tree(nums: List[int]) -> Optional[MaximumBinaryTreeNode]:
        if 0 == len(nums):
            return None

        node = None
        for num in nums:
            if node is None:
                node = MaximumBinaryTreeNode(num)
            else:
                node = node.add(num)

        return node

    # noinspection PyUnresolvedReferences
    def __init__(self, val=0, left: Optional[MaximumBinaryTreeNode] = None,
                 right: Optional[MaximumBinaryTreeNode] = None, weight=1):
        super().__init__(val, left, right, weight)

        self.child_count = 0
        if self.left is not None:
            self.child_count += self.left.child_count
        if self.right is not None:
            self.child_count += self.right.child_count

    # 构建出根就是最大值的二叉树，可以由此展开联想，在构建二叉树的同时，做一些额外操作，得到有特定问题针对性的二叉树。
    def add(self, val: int) -> MaximumBinaryTreeNode:
        if val > self.val:
            return MaximumBinaryTreeNode(val, left=self)

        if val == self.val:
            self.weight += 1
            return self

        self.child_count += 1

        if self.left is None:
            self.left = MaximumBinaryTreeNode(val)
        elif self.right is None:
            self.right = MaximumBinaryTreeNode(val)
        elif self.left.child_count < self.right.child_count:
            self.left = self.left.add(val)
        else:
            self.right = self.right.add(val)

        return self

    def add_node(self, node: MaximumBinaryTreeNode) -> Optional[MaximumBinaryTreeNode]:
        if node is None:
            return self

        self.child_count += node.child_count

        if node.val == self.val:
            self.weight += node.weight

            if self.left is None:
                self.left = node.left
            else:
                self.left = self.left.add_node(node.left)

            if self.right is None:
                self.right = node.right
            else:
                self.right = self.right.add_node(node.right)

            return self

        if node.val > self.val:
            if node.left is None:
                node.left = self
            else:
                # noinspection PyUnresolvedReferences
                node.left = node.left.add_node(self)

            return node

        self.right = node if self.right is None else self.right.add_node(node)

        return self

    def max_value(self) -> int:
        return self.val

    def remove_root(self) -> Optional[MaximumBinaryTreeNode]:
        self.weight -= 1
        if self.weight > 0:
            return self

        if self.left is None:
            return self.right
        elif self.right is None:
            return self.left

        return self.left.add_node(self.right)


class TestMaximumBinaryTree(unittest.TestCase):
    def test_basic(self):
        tree = MaximumBinaryTreeNode.construct_maximum_binary_tree([3, 2, 1, 6, 0, 5])
        nums = tree.level_order_traversal_for_value()
        print(nums)
        self.assertEqual(tree.val, 6)

    def test_minimum(self):
        tree = MaximumBinaryTreeNode.construct_maximum_binary_tree([3, 2, 1])
        nums = tree.level_order_traversal_for_value()
        print(nums)
        self.assertEqual(tree.val, 3)

    def test_single(self):
        tree = MaximumBinaryTreeNode.construct_maximum_binary_tree([7])
        nums = tree.level_order_traversal_for_value()

        self.assertEqual(tree.val, 7)
        self.assertTrue(tree.left is None)
        self.assertTrue(tree.right is None)
        self.assertEqual(nums, [7])


if __name__ == '__main__':
    unittest.main()
