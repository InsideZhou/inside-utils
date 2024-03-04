#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from typing import List


def squared_sum(nums: List[int]) -> int:
    """
    adjust calculation based on my implementation of leetcode maximum_subarray.
    the implementation is based on dynamic programming.
    at any given index in list, current sum is the maximum value between accumulated sum and previous sum.
    while accumulated sum is the maximum value between previous accumulated sum plus current num and current num.
    """
    if len(nums) == 0:
        return 0

    result, accumulated = nums[0], nums[0]
    for num in nums[1:]:
        accumulated = max(accumulated + num, num)
        result = max(accumulated, result)

    return pow(result, 2)


class TestSquaredSum(unittest.TestCase):
    def testBasic1(self):
        self.assertEqual(1, squared_sum([1, -1, 1, -1, 1]))

    def testEmptyList(self):
        self.assertEqual(0, squared_sum([]))

    def testZeroList(self):
        self.assertEqual(0, squared_sum([0] * 100))

    def testAllPositive(self):
        self.assertEqual(36, squared_sum([1, 2, 3]))

    def testAllSamePositive(self):
        self.assertEqual(9, squared_sum([1, 1, 1]))

    def testAllNegative(self):
        self.assertEqual(1, squared_sum([-1, -2, -3]))

    def testAllSameNegative(self):
        self.assertEqual(9, squared_sum([-3, -3, -3]))


if __name__ == '__main__':
    unittest.main()
