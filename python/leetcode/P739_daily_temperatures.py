#!/usr/bin/env python
# https://leetcode.cn/problems/daily-temperatures/
from __future__ import annotations

import unittest
from typing import List


class TemperatureNode:
    def __init__(self, index: int, val: int):
        self.val = val
        self.indexes = [index]

    def merge_same_value_node(self, node: TemperatureNode):
        self.indexes.extend(node.indexes)


def daily_temperatures(temperatures: List[int]) -> List[int]:
    sorted_candidates = []

    def insert_candidate(node: TemperatureNode) -> int:
        candidates_length = len(sorted_candidates)
        if candidates_length == 0:
            sorted_candidates.append(node)
            return 0

        if sorted_candidates[0].val > node.val:
            sorted_candidates.insert(0, node)
            return 0
        elif sorted_candidates[0].val == node.val:
            sorted_candidates[0].merge_same_value_node(node)
            return 0

        if sorted_candidates[-1].val < node.val:
            sorted_candidates.append(node)
            return candidates_length

        start, end = 0, candidates_length - 1

        position = end // 2
        while True:
            prev = sorted_candidates[position - 1]
            pivot = sorted_candidates[position]
            after = sorted_candidates[position + 1]
            if prev.val < node.val <= pivot.val:
                if node.val == pivot.val:
                    pivot.merge_same_value_node(node)
                else:
                    sorted_candidates.insert(position, node)
                return position

            if pivot.val < node.val <= after.val:
                if node.val == after.val:
                    after.merge_same_value_node(node)
                else:
                    sorted_candidates.insert(position + 1, node)
                return position + 1

            if pivot.val == node.val:
                end = position
                position -= 1
            elif pivot.val > node.val:
                end = position
                position //= 2
            else:
                start = position
                position = (start + end) // 2

    for i, val in enumerate(temperatures):
        inserted_index = insert_candidate(TemperatureNode(i, val))
        matched_candidates = sorted_candidates[0:inserted_index]
        sorted_candidates = sorted_candidates[inserted_index:]

        for c in matched_candidates:
            for idx in c.indexes:
                temperatures[idx] = i - idx

    for c in sorted_candidates:
        for idx in c.indexes:
            temperatures[idx] = 0

    return temperatures


class TestDailyTemperatures(unittest.TestCase):
    def testBasic(self):
        self.assertEqual([1, 1, 0], daily_temperatures([30, 60, 90]))
        self.assertEqual([1, 1, 1, 0], daily_temperatures([30, 40, 50, 60]))
        self.assertEqual([1, 1, 4, 2, 1, 1, 0, 0], daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))

    def testStandard(self):
        self.assertEqual([8, 1, 5, 4, 3, 2, 1, 1, 0, 0], daily_temperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))

    def testRepeat(self):
        self.assertEqual([1, 0, 0, 2, 1, 0, 0, 0, 0, 0], daily_temperatures([34, 80, 80, 34, 34, 80, 80, 80, 80, 34]))

    def testRepeat1(self):
        self.assertEqual([0, 0, 0, 1, 0, 0, 1, 0, 0, 0], daily_temperatures([80, 80, 80, 34, 80, 80, 34, 80, 80, 80]))

    def testRepeat2(self):
        self.assertEqual([0, 1, 0, 0, 0, 0, 0, 0, 0, 0], daily_temperatures([80, 34, 80, 80, 80, 34, 34, 34, 34, 34]))


if __name__ == "__main__":
    unittest.main()
