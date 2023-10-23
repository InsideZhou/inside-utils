#!/usr/bin/env python
# https://leetcode.cn/problems/count-good-nodes-in-binary-tree/
import unittest

from leetcode.P102_binary_tree_level_order_traversal import TreeNode


def good_nodes(root: TreeNode) -> int:
    operator_expand = 1
    operator_eval = 2

    nodes = [(operator_expand, root, root.val)]
    result = []

    while True:
        try:
            operator, node, max_val_to_root = nodes.pop()
        except IndexError:
            break

        if operator == operator_expand:
            if node.right is not None:
                nodes.append((operator_expand, node.right, max(node.val, max_val_to_root)))

            nodes.append((operator_eval, node, max_val_to_root))

            if node.left is not None:
                nodes.append((operator_expand, node.left, max(node.val, max_val_to_root)))

        elif operator == operator_eval and node.val >= max_val_to_root:
            result.append(node)

    return len(result)


class TestCountGoodNodesInBinaryTree(unittest.TestCase):
    def testBasic(self):
        n0 = TreeNode(3)
        n1 = TreeNode(1, n0)

        n2 = TreeNode(1)
        n3 = TreeNode(5)
        n4 = TreeNode(4, n2, n3)

        root = TreeNode(3, n1, n4)

        self.assertEqual(4, good_nodes(root))

    def testBasic1(self):
        n0 = TreeNode(4)
        n1 = TreeNode(2)
        n2 = TreeNode(3, n0, n1)
        root = TreeNode(3, n2)

        self.assertEqual(3, good_nodes(root))


if __name__ == '__main__':
    unittest.main()
