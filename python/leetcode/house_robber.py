#!/usr/bin/env python
# https://leetcode.cn/problems/house-robber/


import unittest
from typing import List


def rob(nums: List[int]) -> int:
    prev_two, prev_one = 0, 0
    for num in nums:
        prev_two, prev_one = prev_one, max(prev_two + num, prev_one)

    return prev_one


class TestHouseRobber(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(4, rob([1, 2, 3, 1]))
        self.assertEqual(12, rob([2, 7, 9, 3, 1]))


if __name__ == '__main__':
    unittest.main()
