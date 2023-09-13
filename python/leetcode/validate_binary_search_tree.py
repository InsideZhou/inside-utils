#!/usr/bin/env python
# https://leetcode.cn/problems/validate-binary-search-tree/
from __future__ import annotations

import unittest
from typing import Optional

from leetcode.binary_tree_level_order_traversal import TreeNode


class BinarySearchTreeNode(TreeNode):
    def add(self, val: int) -> None:
        node = self

        while True:
            node.child_count += 1

            if val < node.val:
                if node.left is None:
                    node.left = BinarySearchTreeNode(val)
                    break
                else:
                    node = node.left
            elif node.val < val:
                if node.right is None:
                    node.right = BinarySearchTreeNode(val)
                    break
                else:
                    node = node.right
            else:
                node.weight += 1
                break

    def add_node(self, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        self.child_count += node.child_count

        if node.val == self.val:
            self.weight += node.weight

            if self.left is None:
                self.left = node.left
            else:
                self.left = self.left.add_node(node.left) if node.left is not None else self.left

            if self.right is None:
                self.right = node.right
            else:
                self.right = self.right.add_node(node.right) if node.right is not None else self.right
        elif node.val < self.val:
            self.left = node if self.left is None else self.left.add_node(node)
        else:
            self.right = node if self.right is None else self.right.add_node(node)

        return self

    def max_value(self) -> int:
        node = self
        while node.right is not None:
            node = node.right

        return node.val

    def min_value(self) -> int:
        node = self
        while node.left is not None:
            node = node.left

        return node.val

    # noinspection PyUnresolvedReferences
    def remove_node(self, key: int) -> Optional[BinarySearchTreeNode]:
        parent = None
        root = self
        node = self
        while node is not None:
            if node.val < key:
                parent = node
                node = node.right
            elif node.val > key:
                parent = node
                node = node.left
            else:
                node.weight -= 1
                if node.weight > 0:
                    break

                if node.right is None:
                    middle_root = node.left
                elif node.left is None:
                    middle_root = node.right
                elif node.left.child_count > node.right.child_count:
                    middle_root = node.left.add_node(node.right)
                else:
                    middle_root = node.right.add_node(node.left)

                if parent is None:
                    root = middle_root
                    break

                if parent.left is node:
                    parent.left = middle_root
                elif parent.right is node:
                    parent.right = middle_root

                break

        return root


# noinspection PyUnresolvedReferences,PyTypeChecker
def is_valid_bst(root: BinarySearchTreeNode) -> bool:
    if root.left is None and root.right is None:
        return True
    elif root.left is None:
        return is_valid_bst(root.right) and root.val < root.right.min_value()
    elif root.right is None:
        return is_valid_bst(root.left) and root.left.max_value() < root.val
    else:
        return is_valid_bst(root.left) and is_valid_bst(
            root.right) and root.left.max_value() < root.val < root.right.min_value()


class TestFlattenBinaryTreeToLinkedList(unittest.TestCase):
    def testSame(self):
        b = BinarySearchTreeNode(2)
        c = BinarySearchTreeNode(2)

        tree = BinarySearchTreeNode(2, b, c)
        self.assertFalse(is_valid_bst(tree))

    def testSimple(self):
        b = BinarySearchTreeNode(1)
        c = BinarySearchTreeNode(3)

        tree = BinarySearchTreeNode(2, b, c)
        self.assertTrue(is_valid_bst(tree))

    def testBasic(self):
        a = BinarySearchTreeNode(3)
        b = BinarySearchTreeNode(6)

        c = BinarySearchTreeNode(4, a, b)
        b = BinarySearchTreeNode(2)

        tree = BinarySearchTreeNode(5, b, c)
        self.assertFalse(is_valid_bst(tree))

    def testStandard(self):
        a = BinarySearchTreeNode(27)
        b = BinarySearchTreeNode(19, right=a)
        c = BinarySearchTreeNode(26, left=b)

        d = BinarySearchTreeNode(56)
        e = BinarySearchTreeNode(47, right=d)

        tree = BinarySearchTreeNode(32, c, e)
        self.assertFalse(is_valid_bst(tree))


if __name__ == '__main__':
    unittest.main()
