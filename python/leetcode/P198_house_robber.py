#!/usr/bin/env python
# https://leetcode.cn/problems/house-robber/


import unittest
from typing import List


def rob(nums: List[int]) -> int:
    """
    对当前房子做出劫掠或跳过的决策之后，都可以视为已处理。
    按顺序每处理一所房子，都会有一个当前的劫掠总金额。
    当前劫掠总金额，取决于此前第二个房子的劫掠加上当前房子能劫掠到的金额，与前一所房子的劫掠总金额相比，哪个更大。
    """

    two_before_current, previous = 0, 0
    for num in nums:
        two_before_current, previous = previous, max(two_before_current + num, previous)

    return previous


class TestHouseRobber(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(4, rob([1, 2, 3, 1]))
        self.assertEqual(12, rob([2, 7, 9, 3, 1]))


if __name__ == '__main__':
    unittest.main()
