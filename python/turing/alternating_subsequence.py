#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List


def alt_subsequence_best(x: List[int]) -> int:
    if 0 == len(x):
        return 0

    candidate_stack = x[:1]
    count = len(candidate_stack)

    for num in x[1:]:
        prev_num = candidate_stack.pop()
        if num != prev_num:
            candidate_stack.append(prev_num)
            candidate_stack.append(num)
            continue

        count = max(count, len(candidate_stack) + 1)
        candidate_stack.clear()
        candidate_stack.append(num)

    return max(count, len(candidate_stack))


def alt_subsequence_best_dp(nums: List[int]) -> int:
    if 0 == len(nums):
        return 0

    result, accumulated, prev = 1, 1, nums[0]
    for n in nums[1:]:
        if n != prev:
            accumulated += 1
        else:
            result = max(result, accumulated)
            accumulated = 1

        prev = n

    return max(result, accumulated)


class TestAlternatingSubsequence(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(5, alt_subsequence_best_dp([0, 1, 0, 1, 0]))

    def testSingleElementList(self):
        self.assertEqual(1, alt_subsequence_best_dp([0]))
        self.assertEqual(1, alt_subsequence_best_dp([1]))

    def testSameElementList(self):
        self.assertEqual(1, alt_subsequence_best_dp([0] * random.randint(2, 100)))
        self.assertEqual(1, alt_subsequence_best_dp([1] * random.randint(2, 100)))

    def testEmptyList(self):
        self.assertEqual(0, alt_subsequence_best_dp([]))

    def testSubSequenceOnTail(self):
        self.assertEqual(5, alt_subsequence_best_dp([0] * random.randint(1, 10000) + [0, 1, 0, 1, 0]))
        self.assertEqual(6, alt_subsequence_best_dp([1] * random.randint(1, 10000) + [0, 1, 0, 1, 0]))

    def testSubSequenceOnHead(self):
        self.assertEqual(5, alt_subsequence_best_dp([0, 1, 0, 1, 0] + [0] * random.randint(1, 10000)))
        self.assertEqual(6, alt_subsequence_best_dp([0, 1, 0, 1, 0] + [1] * random.randint(1, 10000)))

    def testSubSequenceInMiddle(self):
        seq = [0] * random.randint(1, 10000) + [0, 1, 0, 1, 0] + [0] * random.randint(1, 10000)
        self.assertEqual(5, alt_subsequence_best_dp(seq))

        seq = [1] * random.randint(1, 10000) + [0, 1, 0, 1, 0] + [0] * random.randint(1, 10000)
        self.assertEqual(6, alt_subsequence_best_dp(seq))

        seq = [0] * random.randint(1, 10000) + [0, 1, 0, 1, 0] + [1] * random.randint(1, 10000)
        self.assertEqual(6, alt_subsequence_best_dp(seq))

        seq = [1] * random.randint(1, 10000) + [0, 1, 0, 1, 0] + [1] * random.randint(1, 10000)
        self.assertEqual(7, alt_subsequence_best_dp(seq))

    def testMultipleSubSequence(self):
        seq = [0, 1, 0] + [1] * random.randint(1, 10000) + [0, 1, 0, 1, 0] + [1] * random.randint(1, 10000) + [0, 1, 0]
        self.assertEqual(7, alt_subsequence_best_dp(seq))


if __name__ == '__main__':
    unittest.main()
