#!/usr/bin/env python
# https://leetcode.cn/problems/merge-intervals/
import unittest
from collections import deque
from typing import List


# 两个要点：1、移除处理过的区间；2、区间合并。
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


def do_merge(source: List[int], target: List[int]) -> int:
    """
    :return: 0：成功合并；1：候选者在合并目标右侧（大于）；-1候选者在合并目标左侧（小于）。
    """

    source_lower_bound, source_upper_bound = source[0], source[1]
    target_lower_bound, target_upper_bound = target[0], target[1]

    if source_lower_bound > target_upper_bound:
        return 1
    elif source_upper_bound < target_lower_bound:
        return -1

    target[0], target[1] = min(source_lower_bound, target_lower_bound), max(source_upper_bound, target_upper_bound)

    return 0


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    result = [intervals[0]]

    for candidate in intervals[1:]:
        pointer = len(result) - 1

        while -1 < pointer:
            match do_merge(candidate, result[pointer]):
                case 1:
                    result.insert(pointer + 1, candidate)
                    break
                case -1:
                    pointer -= 1
                case 0:
                    candidate, result = result[pointer], result[:pointer] + result[pointer + 1:]
                    pointer -= 1

        else:
            result.insert(0, candidate)

    return result


def sort_then_merge(intervals: List[List[int]]) -> List[List[int]]:
    candidates = sorted(intervals, key=lambda x: x[0])
    result, candidates = candidates[:1], deque(candidates[1:])

    while True:
        try:
            candidate = candidates.popleft()
        except IndexError:
            break
        else:
            match do_merge(candidate, result[-1]):
                case 0:
                    continue
                case _:
                    result.append(candidate)

    return result


class TestMergeIntervals(unittest.TestCase):
    def testBasic1(self):
        self.assertEqual([[1, 6], [8, 10], [15, 18]], merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
        self.assertEqual([[1, 6], [8, 10], [15, 18]], merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
        self.assertEqual([[1, 6], [8, 10], [15, 18]], sort_then_merge([[1, 3], [2, 6], [8, 10], [15, 18]]))

    def testBasic2(self):
        self.assertEqual([[1, 5]], merge([[1, 4], [4, 5]]))
        self.assertEqual([[1, 5]], merge_intervals([[1, 4], [4, 5]]))
        self.assertEqual([[1, 5]], sort_then_merge([[1, 4], [4, 5]]))

    def testBasic3(self):
        self.assertEqual([[0, 5]], merge([[4, 5], [1, 4], [0, 1]]))
        self.assertEqual([[0, 5]], merge_intervals([[4, 5], [1, 4], [0, 1]]))
        self.assertEqual([[0, 5]], sort_then_merge([[4, 5], [1, 4], [0, 1]]))

    def testBasic4(self):
        self.assertEqual([[1, 10]], merge_intervals([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
        self.assertEqual([[1, 10]], sort_then_merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))


if __name__ == '__main__':
    unittest.main()
