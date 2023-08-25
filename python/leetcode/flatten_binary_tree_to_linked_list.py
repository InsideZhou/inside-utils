#!/usr/bin/env python
# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
from __future__ import annotations

import unittest
from typing import Optional

from maximum_binary_tree import TreeNode


def flatten(root: Optional[TreeNode]) -> None:
    if root is None:
        return

    flatten(root.left)
    flatten(root.right)

    left_pointer = root.left
    right_pointer = root.left

    if left_pointer is None:
        return

    root.left = None

    while left_pointer.right is not None:
        left_pointer = left_pointer.right

    left_pointer.right = root.right
    root.right = right_pointer


class TestFlattenBinaryTreeToLinkedList(unittest.TestCase):
    def testBasic(self):
        a = TreeNode(3)
        b = TreeNode(4)
        c = TreeNode(6)

        d = TreeNode(2, a, b)
        e = TreeNode(5, right=c)

        root = TreeNode(1, d, e)

        flatten(root)
        self.assertEqual([1, None, 2, None, 3, None, 4, None, 5, None, 6], root.inorder_traversal())

    def testSimple(self):
        root = TreeNode(0)
        flatten(root)
        self.assertEqual([0], root.inorder_traversal())


if __name__ == '__main__':
    unittest.main()
