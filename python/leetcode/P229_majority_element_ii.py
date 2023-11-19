#!/usr/bin/env python
# https://leetcode.cn/problems/majority-element-ii/

import unittest
from typing import List, Optional


class Candidate:
    def __init__(self, value: int, count=1):
        self.value = value
        self.count = count


# 用摩尔投票法实现，空间复杂度是O(1)
# noinspection PyCompatibility
def majority_element(nums: List[int], threshold=3) -> List[int]:
    candidates: List[Optional[Candidate]] = [None] * (threshold - 1)

    def replace_none(n: int) -> bool:
        for i in range(threshold - 1):
            if candidates[i] is None:
                candidates[i] = Candidate(n)
                return True

        return False

    for num in nums:
        candidate = next((c for c in candidates if c is not None and c.value == num), None)
        if candidate is not None:
            candidate.count += 1
            continue

        if replace_none(num):
            continue

        for j, candidate in enumerate(candidates):
            if candidate is not None:
                candidate.count -= 1
                if candidate.count <= 0:
                    candidates[j] = None

    candidates = [Candidate(value=c.value, count=0) for c in candidates if c is not None]

    for num in nums:
        for candidate in candidates:
            if num == candidate.value:
                candidate.count += 1

    return [c.value for c in candidates if c.count > len(nums) // threshold]


class TestMajorityElementIi(unittest.TestCase):
    def testBasic(self):
        self.assertEqual([3], majority_element([3, 2, 3], 3))
        self.assertEqual([1, 2], majority_element([1, 2], 3))
        self.assertEqual([1], majority_element([4, 2, 1, 1], 3))

    def testSingle(self):
        self.assertEqual([1], majority_element([1], 3))

    def testStandard(self):
        self.assertEqual([1], majority_element([1, 2, 3, 1, 4, 5, 6, 1, 1], 3))
        self.assertEqual([1, 2], majority_element([1, 1, 1, 2, 2, 2, 2, 3, 1, 4, 2, 2, 1, 1], 3))


if __name__ == '__main__':
    unittest.main()
