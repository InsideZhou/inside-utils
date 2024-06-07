#!/usr/bin/env python
# https://leetcode.cn/problems/minimum-size-subarray-sum/

import unittest
from typing import List


def min_sub_array_len(target: int, nums: List[int]) -> int:
    """
    思路就是用一个窗口去遍历集合，这个窗口可调整、滑动。
    """

    window_start, window_end = 0, 0
    min_window_length = 0
    window_sum = nums[0]
    nums_length = len(nums)

    while window_end < nums_length:
        if window_sum >= target:
            current_length = window_end - window_start + 1
            min_window_length = current_length if 0 == min_window_length else min(min_window_length, current_length)

            if min_window_length == 1:
                break
            else:
                window_sum -= nums[window_start]
                window_start += 1
        else:
            window_end += 1
            if window_end < nums_length:
                window_sum += nums[window_end]

    return min_window_length


class TestMinimumSizeSubarraySum(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(2, min_sub_array_len(7, [2, 3, 1, 2, 4, 3]))
        self.assertEqual(1, min_sub_array_len(4, [1, 4, 4]))
        self.assertEqual(0, min_sub_array_len(11, [1, 1, 1, 1, 1, 1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
