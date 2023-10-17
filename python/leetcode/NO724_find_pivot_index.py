#!/usr/bin/env python
# https://leetcode.cn/problems/find-pivot-index/
import unittest
from typing import List


def pivot_index(nums: List[int]) -> int:
    sum_left = 0
    sum_right = sum(nums)

    for i, num in enumerate(nums):
        sum_right -= num

        if sum_left == sum_right:
            return i

        sum_left += num

    return -1


class TestFindPivotIndex(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(3, pivot_index([1, 7, 3, 6, 5, 6]))

    def testSimple(self):
        self.assertEqual(-1, pivot_index([1, 2, 3]))

    def testStandard(self):
        self.assertEqual(0, pivot_index([2, 1, -1]))

    def testStandard2(self):
        self.assertEqual(2, pivot_index([-1, -1, -1, -1, -1, 0]))

    def testStandard3(self):
        self.assertEqual(0, pivot_index([-1, -1, -1, 0, 1, 1]))


if __name__ == '__main__':
    unittest.main()
