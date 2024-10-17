#!/usr/bin/env python
# https://leetcode.cn/problems/majority-element-ii/

import unittest
from typing import List, Optional


class Candidate:
    def __init__(self, value: int, count=1):
        self.value = value
        self.count = count


# noinspection PyCompatibility
def majority_element(nums: List[int], threshold=3) -> List[int]:
    """
    求众数（即从集合中找出相同且数量占比超过阈值t的元素）
    用摩尔投票法实现，空间复杂度是O(1)。
    摩尔投票法的背景有：
    1、满足条件的元素个数（相同的元素都算1个）肯定小于1/t。
    2、仅需要(1/t-1)个空间记录候选元素。
    3、两次遍历集合。第一次预选可能符合条件的元素；第二次确定候选元素是否真的满足。也就是第一次极大的缩小预测范围。
    4、预选时，采用抵消的思路，当从集合中取出元素与候选组做比较时，如果其不在候选组中，则抵消一次候选组的计数，计数已为0无法被抵消时的候选元素被移出候选组。

    """

    candidates: List[Optional[Candidate]] = [None] * (threshold - 1)

    def replace_none(n: int) -> bool:
        for i, c in enumerate(candidates):
            if c is None:
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
