#!/usr/bin/env python
# https://leetcode.cn/problems/delete-node-in-a-bst/
import unittest
from typing import Optional

from leetcode.P98_validate_binary_search_tree import BinarySearchTreeNode


def delete_node(root: Optional[BinarySearchTreeNode], key: int) -> Optional[BinarySearchTreeNode]:
    return root.remove_node(key)


class TestDeleteNodeInABst(unittest.TestCase):
    def testBasic(self):
        root = BinarySearchTreeNode(5)
        root.add(3)
        root.add(6)
        root.add(2)
        root.add(4)
        root.add(7)

        root = delete_node(root, 7)
        self.assertEqual([5, 3, 6, 2, 4], root.level_order_traversal_for_value())

    def testRightUp(self):
        root = BinarySearchTreeNode(5)
        root.add(3)
        root.add(6)
        root.add(2)
        root.add(4)
        root.add(7)

        root = delete_node(root, 3)
        self.assertEqual([5, 4, 6, 2, None, None, 7], root.level_order_traversal_for_value())

    def testLeftUp(self):
        root = BinarySearchTreeNode(5)
        root.add(3)
        root.add(6)
        root.add(2)
        root.add(4)
        root.add(7)
        root.add(1)

        root = delete_node(root, 3)
        self.assertEqual([5, 2, 6, 1, 4, None, 7], root.level_order_traversal_for_value())

    def testSingle(self):
        root = BinarySearchTreeNode(0)
        root = delete_node(root, 0)
        self.assertEqual(None, root)


if __name__ == '__main__':
    unittest.main()
