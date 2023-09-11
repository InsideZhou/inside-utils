#!/usr/bin/env python
# https://leetcode.cn/problems/binary-tree-level-order-traversal/
import unittest
from collections import deque
from typing import Optional, List

from leetcode.validate_binary_search_tree import TreeNode


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
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
