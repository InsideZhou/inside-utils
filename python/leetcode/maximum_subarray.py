#!/usr/bin/env python
# https://leetcode.cn/problems/maximum-subarray/

import unittest
from typing import List


def max_sub_array(nums: List[int]) -> int:
    result, accumulated = nums[0], nums[0]
    for num in nums[1:]:
        accumulated = max(accumulated + num, num)
        result = max(accumulated, result)

    return result


class TestMaximumSubarray(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(6, max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(1, max_sub_array([1]))
        self.assertEqual(23, max_sub_array([5, 4, -1, 7, 8]))

    def testNegative(self):
        self.assertEqual(6, max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(-1, max_sub_array([-1]))


if __name__ == '__main__':
    unittest.main()
