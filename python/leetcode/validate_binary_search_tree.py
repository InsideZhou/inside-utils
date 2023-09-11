#!/usr/bin/env python
# https://leetcode.cn/problems/validate-binary-search-tree/
from __future__ import annotations

import unittest
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None, weight=1):
        self.weight = weight
        self.val = val
        self.left = left
        self.right = right

    def add(self, val: int) -> None:
        node = self

        while True:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
            elif node.val < val:
                if node.right is None:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
            else:
                node.weight += 1
                break

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

    def level_order_traversal_for_value(self) -> List[int]:
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

    def preorder_traversal_for_value(self) -> List[Optional[int]]:
        if self.left is None and self.right is None:
            return [self.val]

        left_list = [None] if self.left is None else self.left.preorder_traversal_for_value()
        right_list = [None] if self.right is None else self.right.preorder_traversal_for_value()

        return [self.val] + left_list + right_list

    def inorder_traversal(self) -> List[TreeNode]:
        operator_expand = 1
        operator_eval = 2

        operators = [operator_expand]
        nodes = [self]
        result = []

        while True:
            try:
                node = nodes.pop()
                operator = operators.pop()
            except IndexError:
                break

            if operator == operator_expand:
                if node.right is not None:
                    nodes.append(node.right)
                    operators.append(operator_expand)

                nodes.append(node)
                operators.append(operator_eval)

                if node.left is not None:
                    nodes.append(node.left)
                    operators.append(operator_expand)
            elif operator == operator_eval:
                result.append(node)

        return result


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
