#!/usr/bin/env python
# https://leetcode.cn/problems/permutations/

import unittest
from typing import List


# 借助不含重复数字的特性，利用分治的思路实现。
def permute(nums: List[int]) -> List[List[int]]:
    nums_length = len(nums)
    if 2 == nums_length:
        return [nums, nums[::-1]]
    elif 1 == nums_length:
        return [nums]

    result = []

    for i in range(nums_length):
        locator = nums[i]
        head_group = nums[:i]
        end_group = nums[i + 1:]

        group = [locator]
        for g in permute(head_group + end_group):
            result.append(group + g)

    return result


class TestPermutations(unittest.TestCase):
    def testBasic(self):
        self.assertEqual([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], permute([1, 2, 3]))

    def testSimple(self):
        self.assertEqual([[0, 1], [1, 0]], permute([0, 1]))
        self.assertEqual([[1]], permute([1]))

    def testStandard(self):
        self.assertEqual([[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2],
                          [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1],
                          [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1],
                          [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]],
                         permute([1, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
