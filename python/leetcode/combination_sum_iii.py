#!/usr/bin/env python
# https://leetcode.cn/problems/combination-sum-iii
import unittest
from typing import List


def combination_sum_iii(k: int, n: int, pool_start=1, pool_end=9) -> List[List[int]]:
    if 1 == k:
        return [[n]] if pool_start <= n <= pool_end else []
    elif k >= n:
        return []

    num_pool = [i for i in range(pool_start, pool_end + 1)]

    minimum, maximum = 0, 0
    for i in range(k):
        minimum += i

    for i in range(pool_end, pool_end - k, -1):
        maximum += i

    if n < minimum or n > maximum:
        return []

    result = []

    for start in range(n):
        candidates = []
        for offset in range(k):
            index = start + offset
            if index == n or index > pool_end - pool_start:
                return result

            candidates.append(num_pool[index])

        sum_candidates = sum(candidates)
        if sum_candidates > n:
            break
        elif sum_candidates == n:
            result.append(candidates[:])
            break

        child_k, child_n, child_pool_start = k - 1, n - candidates[0], candidates[0] + 1
        child_result = combination_sum_iii(child_k, child_n, child_pool_start)
        for c in child_result:
            result.append(candidates[0:1] + c)

    return result


class TestCombinationSumIII(unittest.TestCase):
    def testSimple(self):
        self.assertEqual([[1, 2, 4]], combination_sum_iii(3, 7))

    def testBasic(self):
        self.assertEqual([[1, 2, 6], [1, 3, 5], [2, 3, 4]], combination_sum_iii(3, 9))

    def testEmpty(self):
        self.assertEqual([], combination_sum_iii(4, 1))

    def testK2N18(self):
        self.assertEqual([], combination_sum_iii(2, 18))


if __name__ == '__main__':
    unittest.main()
