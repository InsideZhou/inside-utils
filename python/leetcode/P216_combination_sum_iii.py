#!/usr/bin/env python
# https://leetcode.cn/problems/combination-sum-iii
import unittest
from typing import List


def combination_sum_iii(k: int, n: int, pool_start=1, pool_end=9) -> List[List[int]]:
    if 1 == k:
        return [[n]] if pool_start <= n <= pool_end else []
    elif k >= n:
        return []

    result = []

    for start in range(pool_start, pool_end + 1):
        child_k, child_n, child_pool_start = k - 1, n - start, start + 1
        child_result = combination_sum_iii(child_k, child_n, child_pool_start)

        for c in child_result:
            candidate = [start] + c
            sum_of_combination = sum(candidate)
            if sum_of_combination == n:
                result.append(candidate)
            elif sum_of_combination > n:
                break
        else:
            continue

        break

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

    def testK3N15(self):
        self.assertEqual([[1, 5, 9], [1, 6, 8], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 4, 8], [3, 5, 7], [4, 5, 6]],
                         combination_sum_iii(3, 15))


if __name__ == '__main__':
    unittest.main()
