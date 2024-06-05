#!/usr/bin/env python
# https://leetcode.cn/problems/single-number-ii/

import unittest
from typing import List


def single_number(nums: List[int]) -> int:
    """
    从一堆有规律数中找与众不同的那个，转化为统计这些数的每一位出现过多少次。
    也可以理解为将问题转化为了频谱分析，筛选出异常的频率。
    """
    counter = [0] * 32
    for num in nums:
        for i in range(32):
            counter[i] += (num >> i) & 1

    exists_count = 3
    result = 0
    for i in range(32):
        result |= (counter[i] % exists_count) << i

    # ~(result ^ 0xffffffff) 意思是保持低32位不变，对其余位取反，对python的负数表示做针对性处理。
    return result if counter[31] % exists_count == 0 else ~(result ^ 0xffffffff)


class TestSingleNumberIi(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(3, single_number([2, 2, 3, 2]))
        self.assertEqual(99, single_number([0, 1, 0, 1, 0, 1, 99]))
        self.assertEqual(-7, single_number([0, 1, 0, 1, 0, 1, -7]))


if __name__ == '__main__':
    unittest.main()
