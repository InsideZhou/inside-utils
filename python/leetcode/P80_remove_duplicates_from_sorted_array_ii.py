#!/usr/bin/env python
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/


import unittest
from typing import List

MAX_DUPLICATION_LENGTH = 2


def remove_duplicates(nums: List[int]) -> int:
    """
    利用集合是有序的特性，双指针遍历该集合，主指针确定重复元素的七点，副指针确定重复元素的终点。
    时间复杂度是O(n)，空间复杂度是O(1)。
    """

    duplication_start = 0

    while duplication_start < len(nums):
        duplication_end = duplication_start + 1
        while duplication_end < len(nums) and nums[duplication_end] == nums[duplication_start]:
            duplication_end += 1

        del nums[duplication_start + MAX_DUPLICATION_LENGTH:duplication_end]

        duplication_start += 1

    return len(nums)


class TestRemoveDuplicates(unittest.TestCase):
    def test_basic(self):
        nums = [1, 1, 1, 2, 2, 3]
        expect = [1, 1, 2, 2, 3]
        remain_length = remove_duplicates(nums)

        self.assertEqual(remain_length, len(expect))
        self.assertEqual(nums, expect)

    def test_standard(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        expect = [0, 0, 1, 1, 2, 3, 3]
        remain_length = remove_duplicates(nums)

        self.assertEqual(remain_length, len(expect))
        self.assertEqual(nums, expect)


if __name__ == '__main__':
    unittest.main()
