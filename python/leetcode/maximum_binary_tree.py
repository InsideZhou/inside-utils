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

        node = MaximumBinaryTreeNode(nums[0])
        for num in nums:
            node = node.add(num)

        return node

    # 构建出根就是最大值的二叉树，可以由此展开联想，在构建二叉树的同时，做一些额外操作，得到有特定问题针对性的二叉树。
    def add(self, val: int) -> MaximumBinaryTreeNode:
        if val == self.val:
            self.weight += 1
            return self

        if val > self.val:
            new_node = MaximumBinaryTreeNode(val)
            new_node.left = self
            return new_node

        self.right = MaximumBinaryTreeNode(val) if self.right is None else self.right.add(val)

        return self

    def max_value(self) -> int:
        return self


class TestTreeNode(unittest.TestCase):
    def test_basic(self):
        tree = MaximumBinaryTreeNode.construct_maximum_binary_tree([3, 2, 1, 6, 0, 5])
        nums = tree.level_order_traversal_for_value()

        self.assertEqual(tree.val, 6)
        self.assertEqual(tree.left.val, 3)
        self.assertEqual(tree.right.val, 5)
        self.assertEqual(nums, [6, 3, 5, None, 2, 0, None, None, 1])

    def test_minimum(self):
        tree = MaximumBinaryTreeNode.construct_maximum_binary_tree([3, 2, 1])
        nums = tree.level_order_traversal_for_value()

        self.assertEqual(tree.val, 3)
        self.assertTrue(tree.left is None)
        self.assertEqual(tree.right.val, 2)
        self.assertEqual(nums, [3, None, 2, None, 1])

    def test_single(self):
        tree = MaximumBinaryTreeNode.construct_maximum_binary_tree([7])
        nums = tree.level_order_traversal_for_value()

        self.assertEqual(tree.val, 7)
        self.assertTrue(tree.left is None)
        self.assertTrue(tree.right is None)
        self.assertEqual(nums, [7])


if __name__ == '__main__':
    unittest.main()
