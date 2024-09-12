#!/usr/bin/env python
# https://leetcode.cn/problems/binary-tree-level-order-traversal/
from __future__ import annotations

import unittest
from collections import deque
from typing import Optional, List


class TreeNode(object):
    @staticmethod
    def construct_binary_tree_from_values(values: List[Optional[int]]) -> TreeNode:
        value_queue = deque(values)
        root = TreeNode(value_queue.popleft())
        candidates = deque([root])

        while True:
            try:
                node = candidates.popleft()

                left = value_queue.popleft()
                if left is not None:
                    node.left = TreeNode(left)
                    candidates.append(node.left)

                right = value_queue.popleft()
                if right is not None:
                    node.right = TreeNode(right)
                    candidates.append(node.right)
            except IndexError:
                break

        return root

    # noinspection PyUnresolvedReferences
    def __init__(self, val=0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None, weight=1):
        self.weight = weight
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return ",".join([str(item) for item in self.level_order_traversal_for_value()])

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

    def level_order_traversal_for_value(self) -> List[Optional[int]]:
        """
        仅生成节点值的层序遍历，结果数组中间空值用None表示，末尾空值全部舍去。
        """

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


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    生成二维数组的层序遍历。
    """

    result = []
    current_level, level_group = 0, []
    nodes = deque([(current_level, root)])

    while True:
        try:
            level, node = nodes.popleft()
            next_level = level + 1

            if level > current_level:
                result.append([item for item in level_group if item is not None])
                current_level = level
                level_group = []

            if node is None:
                level_group.append(None)
                continue

            # noinspection PyUnresolvedReferences
            level_group.append(node.val)
            nodes.append((next_level, node.left))
            nodes.append((next_level, node.right))
        except IndexError:
            break
        finally:
            if all([n is None for _, n in nodes]):
                level_group = [item for item in level_group if item is not None]
                if len(level_group) > 0:
                    result.append(level_group)

                break

    return result


class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):
    def testEmpty(self):
        self.assertEqual([], level_order(None))

    def testSimple(self):
        e = TreeNode(1)

        self.assertEqual([[1]], level_order(e))

    def testStandard(self):
        a = TreeNode(15)
        b = TreeNode(7)
        c = TreeNode(20, a, b)
        d = TreeNode(9)
        e = TreeNode(3, d, c)

        self.assertEqual([[3], [9, 20], [15, 7]], level_order(e))


if __name__ == '__main__':
    unittest.main()
