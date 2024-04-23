#!/usr/bin/env python
# https://leetcode.cn/problems/maximum-alternating-subsequence-sum

import unittest
from typing import List


def max_alternating_sum(nums: List[int]) -> int:
    max_sum, prev_min_num, last_num = nums[0], None, nums[0]

    for i, num in enumerate(nums[1:]):
        if prev_min_num is None:
            if num > last_num:
                max_sum += num - last_num
                last_num = num
            else:
                prev_min_num = num
        elif prev_min_num > num:
            prev_min_num = num
        elif prev_min_num < num:
            max_sum += num - prev_min_num
            prev_min_num, last_num = None, num

    return max_sum


class TestMaxAlternatingSubsequenceSum(unittest.TestCase):
    def testBasic1(self):
        self.assertEqual(7, max_alternating_sum([4, 2, 5, 3]))

    def testBasic2(self):
        self.assertEqual(8, max_alternating_sum([5, 6, 7, 8]))

    def testBasic3(self):
        self.assertEqual(10, max_alternating_sum([6, 2, 1, 2, 4, 5]))

    def testBasic4(self):
        self.assertEqual(13, max_alternating_sum([4, 9, 7, 4, 8]))

    def testBasic5(self):
        self.assertEqual(31, max_alternating_sum([3, 2, 8, 10, 3, 8, 4, 13, 9, 15]))


if __name__ == '__main__':
    unittest.main()
