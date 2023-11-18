#!/usr/bin/env python
# https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/
import unittest
from typing import Optional, List, Tuple

from leetcode.P102_binary_tree_level_order_traversal import TreeNode


def longest_zigzag(root: Optional[TreeNode]) -> int:
    longest_visited = [0]
    left, right, start = "left", "right", "start"

    def moving(node: TreeNode, previous_path: str, count: int):
        if node is None:
            longest_visited[0] = max(longest_visited[0], count)
            return

        match previous_path:
            case "left":
                moving(node.left, left, 1)
                moving(node.right, right, count + 1)
            case "right":
                moving(node.left, left, count + 1)
                moving(node.right, right, 1)
            case "start":
                moving(node.left, left, 1)
                moving(node.right, right, 1)

    moving(root, start, 0)

    return longest_visited[0] - 1


class TestLongestZigzagPathInBinaryTree(unittest.TestCase):
    def testBasic(self):
        tree = TreeNode.construct_binary_tree_from_values(
            [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
        )
        self.assertEqual(3, longest_zigzag(tree))

    def testBasic1(self):
        tree = TreeNode.construct_binary_tree_from_values(
            [1, 1, 1, None, 1, None, None, 1, 1, None, 1]
        )
        self.assertEqual(4, longest_zigzag(tree))

    def testSingle(self):
        self.assertEqual(0, longest_zigzag(TreeNode(1)))


if __name__ == '__main__':
    unittest.main()
