#!/usr/bin/env python
# https://leetcode.cn/problems/triangle/
import unittest
from typing import List


def minimum_total(triangle: List[List[int]]) -> int:
    """
    在第N行时，该行每一个元素都表示一条或多条可能的路径，要得到值最小的路径，必须是当前行每个元素与前一行的路径值相加，其中最小的就是当前的最小路径。
    """

    row: List[int] = triangle[0]

    for i in range(1, len(triangle)):
        upper = row
        row = triangle[i]
        row_length = len(row)

        for j in range(row_length):
            if 0 == j:
                row[j] = upper[j] + row[j]
            elif j == row_length - 1:
                row[j] = upper[j - 1] + row[j]
            else:
                row[j] = min(upper[j - 1] + row[j], upper[j] + row[j])

    return min(row)


class TestTriangle(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(11, minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
        self.assertEqual(-10, minimum_total([[-10]]))


if __name__ == '__main__':
    unittest.main()
