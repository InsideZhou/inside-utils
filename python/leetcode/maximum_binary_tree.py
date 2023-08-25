#!/usr/bin/env python
# https://leetcode.cn/problems/maximum-binary-tree/
from __future__ import annotations

import unittest
from typing import Optional, List


class TreeNode:
    @staticmethod
    def construct_maximum_binary_tree(nums: List[int]) -> Optional[TreeNode]:
        if 0 == len(nums):
            return None

        node = TreeNode(nums[0])
        for num in nums:
            node = node.__add(num)

        return node

    def __init__(self, val=0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right

    def __add(self, val: int) -> TreeNode:
        if val == self.val:
            return self

        if val > self.val:
            new_node = TreeNode(val)
            new_node.left = self
            return new_node

        self.right = TreeNode(val) if self.right is None else self.right.__add(val)

        return self

    def max_value(self) -> int:
        candidates = [self.val]

        if self.left is not None:
            candidates.append(self.left.max_value())

        if self.right is not None:
            candidates.append(self.right.max_value())

        return max(candidates)

    def min_value(self) -> int:
        candidates = [self.val]

        if self.left is not None:
            candidates.append(self.left.min_value())

        if self.right is not None:
            candidates.append(self.right.min_value())

        return min(candidates)

    def is_valid_bst(self) -> bool:
        if self.left is None and self.right is None:
            return True
        elif self.left is None:
            return self.right.is_valid_bst() and self.val < self.right.min_value()
        elif self.right is None:
            return self.left.is_valid_bst() and self.left.max_value() < self.val
        else:
            return self.left.is_valid_bst() and self.right.is_valid_bst() and self.left.max_value() < self.val < self.right.min_value()

    def level_order_traversal(self) -> List[int]:
        nums = []
        nodes = [self]

        while True:
            try:
                node = nodes.pop()

                if node is None:
                    nums.append(None)
                    continue

                nums.append(node.val)
                nodes.insert(0, node.left)
                nodes.insert(0, node.right)
            except IndexError:
                break
            finally:
                if all([n is None for n in nodes]):
                    break

        return nums

    def inorder_traversal(self) -> List[Optional[int]]:
        if self.left is None and self.right is None:
            return [self.val]

        left_list = [None] if self.left is None else self.left.inorder_traversal()
        right_list = [None] if self.right is None else self.right.inorder_traversal()

        return [self.val] + left_list + right_list


class TestTreeNode(unittest.TestCase):
    def test_basic(self):
        tree = TreeNode.construct_maximum_binary_tree([3, 2, 1, 6, 0, 5])
        nums = tree.level_order_traversal()

        self.assertEqual(tree.val, 6)
        self.assertEqual(tree.left.val, 3)
        self.assertEqual(tree.right.val, 5)
        self.assertEqual(nums, [6, 3, 5, None, 2, 0, None, None, 1])

    def test_minimum(self):
        tree = TreeNode.construct_maximum_binary_tree([3, 2, 1])
        nums = tree.level_order_traversal()

        self.assertEqual(tree.val, 3)
        self.assertTrue(tree.left is None)
        self.assertEqual(tree.right.val, 2)
        self.assertEqual(nums, [3, None, 2, None, 1])

    def test_single(self):
        tree = TreeNode.construct_maximum_binary_tree([7])
        nums = tree.level_order_traversal()

        self.assertEqual(tree.val, 7)
        self.assertTrue(tree.left is None)
        self.assertTrue(tree.right is None)
        self.assertEqual(nums, [7])


if __name__ == '__main__':
    unittest.main()
