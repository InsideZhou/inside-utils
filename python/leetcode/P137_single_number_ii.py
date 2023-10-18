#!/usr/bin/env python
# https://leetcode.cn/problems/single-number-ii/

import unittest
from typing import List


# 从一堆有规律数中找不同的那个，可以适当在二进制层面考虑，整体逻辑可能会非常短。
def single_number(nums: List[int]) -> int:
    counter = [0] * 32
    for num in nums:
        for i in range(32):
            counter[i] += (num >> i) & 1

    exists_count = 3
    result = 0
    for i in range(32):
        result |= (counter[i] % exists_count) << i

    # ~(result ^ 0xffffffff) 意思是低32位不变，对其余位取反，对python的负数表示做针对性处理。
    return result if counter[31] % exists_count == 0 else ~(result ^ 0xffffffff)


class TestSingleNumberIi(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(3, single_number([2, 2, 3, 2]))
        self.assertEqual(99, single_number([0, 1, 0, 1, 0, 1, 99]))


if __name__ == '__main__':
    unittest.main()
