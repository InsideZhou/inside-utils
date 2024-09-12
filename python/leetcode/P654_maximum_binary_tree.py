#!/usr/bin/env python
# https://leetcode.cn/problems/maximum-binary-tree/
from __future__ import annotations

import unittest
from typing import Optional, List

from leetcode.P102_binary_tree_level_order_traversal import TreeNode


class MaximumBinaryTreeNode(TreeNode):
    @staticmethod
    def construct_maximum_binary_tree(nums: List[int]) -> Optional[MaximumBinaryTreeNode]:
        if 0 == len(nums):
            return None

        node = MaximumBinaryTreeNode(nums[0])
        for num in nums[1:]:
            node = node.add(num)

        return node

    def __str__(self):
        values = self.level_order_traversal_for_value()
        values_count, height = len(values), 0
        result = ""
        for idx, item in enumerate(self.level_order_traversal_for_value()):
            if idx == values_count - 1:
                result += f"{item}\n"
            elif idx == pow(2, height) - 1:
                result += f"{item}\n"
                height += 1
            else:
                result += f"{item},"

        return result

    def max_value(self) -> int:
        return self.val

    # 构建出根就是最大值的二叉树，可以由此展开联想，在构建二叉树的同时，做一些额外操作，得到有特定问题针对性的二叉树。
    def add(self, val: int) -> MaximumBinaryTreeNode:
        return self.add_node(MaximumBinaryTreeNode(val))

    def add_node(self, node: MaximumBinaryTreeNode) -> MaximumBinaryTreeNode:
        """
        假设了所添加节点是单节点，无下级节点。
        确保每一个节点的左子节点值小于其右子节点。
        """

        cursor, parent = self, None

        while True:
            if cursor.val < node.val:
                node.left = cursor

                if parent is None:
                    return node

                if cursor == parent.left:
                    parent.left = node
                else:
                    parent.right = node

                return self
            elif cursor.val == node.val:
                cursor.weight += node.weight
                return self
            elif cursor.right is None and cursor.left is None:
                cursor.left = node
                return self
            elif cursor.right is None:
                if node.val > cursor.left.val:
                    cursor.right = node
                else:
                    cursor.right = cursor.left
                    cursor.left = node

                return self
            elif cursor.left is None:
                if node.val > cursor.right.val:
                    cursor.left = cursor.right
                    cursor.right = node
                else:
                    cursor.left = node

                return self
            elif cursor.left.val < node.val <= cursor.right.val:
                cursor, parent = cursor.right, cursor
            else:
                cursor, parent = cursor.left, cursor

    def merge(self, node: MaximumBinaryTreeNode) -> MaximumBinaryTreeNode:
        root = self

        if node is None:
            return root

        if root.val == node.val:
            root.weight += node.weight
            root.left = node.left if root.left is None else root.left.merge(node.left)
            root.right = node.right if root.right is None else root.right.merge(node.right)
        else:
            if root.val < node.val:
                root, node = node, root

            if node.val % 2 == 0:
                root.right = node if root.right is None else root.right.merge(node)
            else:
                root.left = node if root.left is None else root.left.merge(node)

        return root

    def remove_root(self) -> Optional[MaximumBinaryTreeNode]:
        self.weight -= 1
        if self.weight > 0:
            return self

        if self.left is None:
            return self.right

        if self.right is None:
            return self.left

        return self.right.merge(self.left)


class TestMaximumBinaryTree(unittest.TestCase):
    def test_basic(self):
        tree = MaximumBinaryTreeNode.construct_maximum_binary_tree([3, 2, 1, 6, 0, 5])
        self.assertEqual(tree.val, 6)

    def test_minimum(self):
        tree = MaximumBinaryTreeNode.construct_maximum_binary_tree([3, 2, 1])
        self.assertEqual(tree.val, 3)

    def test_single(self):
        tree = MaximumBinaryTreeNode.construct_maximum_binary_tree([7])
        nums = tree.level_order_traversal_for_value()

        self.assertEqual(tree.val, 7)
        self.assertTrue(tree.left is None)
        self.assertTrue(tree.right is None)
        self.assertEqual(nums, [7])


if __name__ == '__main__':
    unittest.main()
