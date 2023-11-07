#!/usr/bin/env python
# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
from __future__ import annotations

import unittest
from typing import Optional

from leetcode.P98_validate_binary_search_tree import BinarySearchTreeNode


def flatten(root: Optional[BinarySearchTreeNode]) -> None:
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
        a = BinarySearchTreeNode(3)
        b = BinarySearchTreeNode(4)
        c = BinarySearchTreeNode(6)

        d = BinarySearchTreeNode(2, a, b)
        e = BinarySearchTreeNode(5, right=c)

        root = BinarySearchTreeNode(1, d, e)

        flatten(root)
        self.assertEqual([1, None, 2, None, 3, None, 4, None, 5, None, 6], root.preorder_traversal_for_value())

    def testSimple(self):
        root = BinarySearchTreeNode(0)
        flatten(root)
        self.assertEqual([0], root.preorder_traversal_for_value())


if __name__ == '__main__':
    unittest.main()
