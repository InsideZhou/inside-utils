#!/usr/bin/env python
# https://leetcode.cn/problems/search-in-a-binary-search-tree/
import unittest

from leetcode.P98_validate_binary_search_tree import BinarySearchTreeNode


class TestSearchInABinarySearchTree(unittest.TestCase):
    def testMatch(self):
        tree = BinarySearchTreeNode(4)
        tree.add(2)
        tree.add(7)
        tree.add(1)
        tree.add(3)

        tree = tree.find_value(2)
        self.assertEqual([2, 1, 3], tree.level_order_traversal_for_value())

    def testNonMatch(self):
        tree = BinarySearchTreeNode(4)
        tree.add(2)
        tree.add(7)
        tree.add(1)
        tree.add(3)

        tree = tree.find_value(5)
        self.assertEqual(None, tree)


if __name__ == '__main__':
    unittest.main()
