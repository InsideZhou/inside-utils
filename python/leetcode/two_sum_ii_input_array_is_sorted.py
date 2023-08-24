#!/usr/bin/env python
# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
import unittest
from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    """

    :param numbers: 必须是非递减顺序排列，元素数量不少于2
    :param target: 求和的目标值
    """
    index_b = 1
    index_a = index_b - 1

    numbers_length = len(numbers)

    while index_b < numbers_length and numbers[index_a] + numbers[index_b] < target:
        index_b += 2
        index_a = index_b - 1

    while index_b >= numbers_length:
        index_b -= 1

    index_locator = index_b
    index_a = index_b - 1

    while index_locator >= 1:
        current_sum = numbers[index_a] + numbers[index_b]
        if current_sum == target:
            return [index_a + 1, index_b + 1]
        elif current_sum > target:
            index_a -= 1
        else:
            index_b += 1

        if index_a < 0 or index_b == numbers_length:
            index_locator -= 1
            index_b = index_locator
            index_a = index_b - 1

    return [0, 0]


class TestTowSumII(unittest.TestCase):
    def test_basic(self):
        self.assertEqual([4, 5], two_sum([2, 3, 4, 7, 10, 11, 12], 17))
        self.assertEqual([1, 2], two_sum([2, 7, 11, 15], 9))
        self.assertEqual([1, 3], two_sum([2, 3, 4], 6))
        self.assertEqual([1, 2], two_sum([-1, 0], -1))

    def test_standard(self):
        self.assertEqual([24, 32], two_sum(
            [12, 13, 23, 28, 43, 44, 59, 60, 61, 68, 70, 86, 88, 92, 124, 125, 136, 168, 173, 173, 180, 199, 212, 221,
             227, 230, 277, 282, 306, 314, 316, 321, 325, 328, 336, 337, 363, 365, 368, 370, 370, 371, 375, 384, 387,
             394, 400, 404, 414, 422, 422, 427, 430, 435, 457, 493, 506, 527, 531, 538, 541, 546, 568, 583, 585, 587,
             650, 652, 677, 691, 730, 737, 740, 751, 755, 764, 778, 783, 785, 789, 794, 803, 809, 815, 847, 858, 863,
             863, 874, 887, 896, 916, 920, 926, 927, 930, 933, 957, 981, 997], 542))


if __name__ == '__main__':
    unittest.main()
