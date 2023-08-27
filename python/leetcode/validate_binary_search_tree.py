#!/usr/bin/env python
# https://leetcode.cn/problems/validate-binary-search-tree/
from __future__ import annotations

import unittest

from maximum_binary_tree import TreeNode


class TestFlattenBinaryTreeToLinkedList(unittest.TestCase):
    def testSame(self):
        b = TreeNode(2)
        c = TreeNode(2)

        tree = TreeNode(2, b, c)
        self.assertFalse(tree.is_valid_bst())

    def testSimple(self):
        b = TreeNode(1)
        c = TreeNode(3)

        tree = TreeNode(2, b, c)
        self.assertTrue(tree.is_valid_bst())

    def testBasic(self):
        a = TreeNode(3)
        b = TreeNode(6)

        c = TreeNode(4, a, b)
        b = TreeNode(2)

        tree = TreeNode(5, b, c)
        self.assertFalse(tree.is_valid_bst())

    def testStandard(self):
        a = TreeNode(27)
        b = TreeNode(19, right=a)
        c = TreeNode(26, left=b)

        d = TreeNode(56)
        e = TreeNode(47, right=d)

        tree = TreeNode(32, c, e)
        self.assertFalse(tree.is_valid_bst())


if __name__ == '__main__':
    unittest.main()
