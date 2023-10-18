#!/usr/bin/env python
# https://leetcode.cn/problems/house-robber/


import unittest
from typing import List


# 每次计算时，必须的依赖已经由上游完成计算，并注入到当前上下文中。
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
