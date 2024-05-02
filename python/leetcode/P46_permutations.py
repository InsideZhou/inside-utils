#!/usr/bin/env python
# https://leetcode.cn/problems/permutations/

import unittest
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """
    利用分治算法。一个集合元素的全排列，可以按以下思路获得：
    1、集合内每个元素（设为A）加上其剩余元素全排列，可以得到一组排列，可以说该排列是按A分类的。
    2、按并集合并上一步得到的所有组。
    3、得到该集合元素全排列的结果。
    """

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
