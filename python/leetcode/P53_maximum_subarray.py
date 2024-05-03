#!/usr/bin/env python
# https://leetcode.cn/problems/maximum-subarray/

import unittest
from typing import List


def max_sub_array_with_all_steps(nums: List[int]) -> int:
    result = [0] * len(nums)
    result[0] = nums[0]

    for i in range(1, len(nums)):
        result[i] = max(nums[i], result[i - 1] + nums[i])

    return max(result)


def max_sub_array(nums: List[int]) -> int:
    max_result, result = nums[0], nums[0]
    for num in nums[1:]:
        result = max(result + num, num)
        max_result = max(result, max_result)

    return max_result


class TestMaximumSubarray(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(6, max_sub_array_with_all_steps([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(6, max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

        self.assertEqual(1, max_sub_array_with_all_steps([1]))
        self.assertEqual(1, max_sub_array([1]))

        self.assertEqual(23, max_sub_array_with_all_steps([5, 4, -1, 7, 8]))
        self.assertEqual(23, max_sub_array([5, 4, -1, 7, 8]))

    def testNegative(self):
        self.assertEqual(6, max_sub_array_with_all_steps([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(6, max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

        self.assertEqual(-1, max_sub_array_with_all_steps([-1]))
        self.assertEqual(-1, max_sub_array([-1]))


if __name__ == '__main__':
    unittest.main()
