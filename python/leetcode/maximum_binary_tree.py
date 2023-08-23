#!/usr/bin/env python
from __future__ import annotations

import unittest
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    @staticmethod
    def construct_maximum_binary_tree(nums: List[int]) -> Optional[TreeNode]:
        if 0 == len(nums):
            return None

        node = TreeNode(nums[0])
        for num in nums:
            node = node.add(num)

        return node

    def __init__(self, val=0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right

    def add(self, val: int) -> TreeNode:
        if val == self.val:
            return self

        if val > self.val:
            new_node = TreeNode(val)
            new_node.left = self
            return new_node

        self.right = TreeNode(val) if self.right is None else self.right.add(val)

        return self

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
