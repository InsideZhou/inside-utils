#!/usr/bin/env python
# https://leetcode.cn/problems/path-sum-iii/
import unittest
from typing import Optional, List

from leetcode.P102_binary_tree_level_order_traversal import TreeNode


def path_sum(root: Optional[TreeNode], target_sum: int) -> int:
    if root is None:
        return 0

    result = []

    def node_cal(node: TreeNode, parent_sums: List):
        effective_sums = [node.val + val for val in parent_sums]
        effective_sums.append(node.val)

        for i, value in enumerate(effective_sums):
            if value == target_sum:
                result.append((i, node.val))

        if node.left is not None:
            node_cal(node.left, effective_sums)

        if node.right is not None:
            node_cal(node.right, effective_sums)

    node_cal(root, [])

    return len(result)


class TestPathSumIII(unittest.TestCase):
    def testBasic(self):
        tree = TreeNode.construct_binary_tree_from_values([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
        self.assertEqual(3, path_sum(tree, 8))

    def testBasic1(self):
        tree = TreeNode.construct_binary_tree_from_values([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
        self.assertEqual(3, path_sum(tree, 22))

    def testEmpty(self):
        tree = None
        self.assertEqual(0, path_sum(tree, 8))

    def testSingle(self):
        tree = TreeNode(1)
        self.assertEqual(0, path_sum(tree, 0))

    def testNegative(self):
        tree = TreeNode.construct_binary_tree_from_values([-2, None, -3])
        self.assertEqual(1, path_sum(tree, -3))

    def testMultipleMatchInOnePath(self):
        tree = TreeNode.construct_binary_tree_from_values([0, 1, 1])
        self.assertEqual(4, path_sum(tree, 1))


if __name__ == '__main__':
    unittest.main()
