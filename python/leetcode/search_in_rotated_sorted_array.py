#!/usr/bin/env python
# https://leetcode.cn/problems/search-in-rotated-sorted-array/
import unittest
from typing import List


def search(nums: List[int], target: int) -> int:
    nums_length = len(nums)

    if 1 == nums_length:
        return -1 if nums[0] != target else 0
    elif 0 == nums_length:
        return -1

    split_index = len(nums) // 2
    left_part = nums[0:split_index]
    right_part = nums[split_index:]

    # 折半查找的同时，利用数据集有序且互不相同的性质，排除无需处理的子集。
    if not (split_index > 1 and left_part[0] < left_part[-1] and (target < left_part[0] or target > left_part[-1])):
        left_index = search(left_part, target)
        if -1 != left_index:
            return left_index

    if not (split_index > 1 and right_part[0] < right_part[-1] and (target < right_part[0] or target > right_part[-1])):
        right_index = search(right_part, target)
        if -1 != right_index:
            return right_index + split_index

    return -1


class TestSearchInRotatedSortedArray(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(5, search([4, 5, 6, 7, 0, 1, 2], 1))
        self.assertEqual(4, search([4, 5, 6, 7, 0, 1, 2], 0))
        self.assertEqual(-1, search([4, 5, 6, 7, 0, 1, 2], 3))
        self.assertEqual(-1, search([1], 0))
        self.assertEqual(0, search([1, 3, 5], 1))


if __name__ == '__main__':
    unittest.main()
