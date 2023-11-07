#!/usr/bin/env python
# https://leetcode.cn/problems/kth-largest-element-in-an-array/
import unittest
from typing import List

from leetcode.P654_maximum_binary_tree import MaximumBinaryTreeNode


def find_kth_largest(nums: List[int], k: int) -> int:
    tree = MaximumBinaryTreeNode.construct_maximum_binary_tree(nums)
    for i in range(1, k):
        tree = tree.remove_root()

    return tree.max_value()


class TestKthLargestElementInAnArray(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(1, find_kth_largest([2, 1], 2))

    def testStandard(self):
        self.assertEqual(5, find_kth_largest([3, 2, 1, 5, 6, 4], 2))
        self.assertEqual(4, find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

    def testContainsZero(self):
        self.assertEqual(3, find_kth_largest([5, 2, 4, 1, 3, 6, 0], 4))

    def testLong(self):
        self.assertEqual(2, find_kth_largest(
            [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6], 20))


if __name__ == '__main__':
    unittest.main()
