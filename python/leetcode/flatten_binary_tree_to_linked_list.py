#!/usr/bin/env python
# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
from __future__ import annotations

import unittest
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right

    def to_value_list(self) -> List[Optional[int]]:
        if self.left is None and self.right is None:
            return [self.val]

        left_list = [None] if self.left is None else self.left.to_value_list()
        right_list = [None] if self.right is None else self.right.to_value_list()

        return [self.val] + left_list + right_list


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
        self.assertEqual([1, None, 2, None, 3, None, 4, None, 5, None, 6], root.to_value_list())

    def testSimple(self):
        root = TreeNode(0)
        flatten(root)
        self.assertEqual([0], root.to_value_list())


if __name__ == '__main__':
    unittest.main()
