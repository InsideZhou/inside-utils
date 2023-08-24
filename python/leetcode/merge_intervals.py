#!/usr/bin/env python
# https://leetcode.cn/problems/merge-intervals/
import unittest
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    result = []

    while True:
        try:
            interval = intervals.pop(0)
        except IndexError:
            break

        lower_bound, upper_bound = interval[0], interval[1]

        while True:
            consumed_intervals = []
            for i in intervals:
                lower_candidate, upper_candidate = i[0], i[1]
                if not lower_candidate > upper_bound and not lower_bound > upper_candidate:
                    lower_bound = min(lower_bound, lower_candidate)
                    upper_bound = max(upper_bound, upper_candidate)
                    consumed_intervals.append(i)

            if len(consumed_intervals) > 0:
                for i in consumed_intervals:
                    intervals.remove(i)
            else:
                result.append([lower_bound, upper_bound])
                break

    return result


class TestMergeIntervals(unittest.TestCase):
    def test_basic(self):
        self.assertEqual([[1, 6], [8, 10], [15, 18]], merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
        self.assertEqual([[1, 5]], merge([[1, 4], [4, 5]]))
        self.assertEqual([[0, 5]], merge([[4, 5], [1, 4], [0, 1]]))


if __name__ == '__main__':
    unittest.main()
