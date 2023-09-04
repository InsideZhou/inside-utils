#!/usr/bin/env python
# https://leetcode.cn/problems/number-of-islands/
import unittest
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    rows_count = len(grid)
    result = 0

    def destroy_island(row: int, col: int):
        grid[row][col] = '0'

        up = (row - 1, col) if row > 0 else None
        down = (row + 1, col) if row < rows_count - 1 else None
        left = (row, col - 1) if col > 0 else None
        right = (row, col + 1) if col < len(grid[row]) - 1 else None

        for r, c in [item for item in [up, down, left, right] if item is not None]:
            if '1' == grid[r][c]:
                destroy_island(r, c)

    for i in range(rows_count):
        for j in range(len(grid[i])):
            if '1' == grid[i][j]:
                result += 1
                destroy_island(i, j)

    return result


class TestNumberOfIslands(unittest.TestCase):
    def testSimple(self):
        grid = [
            ["1", "1", "1"],
            ["0", "1", "0"],
            ["1", "1", "1"]
        ]

        self.assertEqual(1, num_islands(grid))

    def testBasic(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]

        self.assertEqual(1, num_islands(grid))

    def testStandard(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]

        self.assertEqual(3, num_islands(grid))


if __name__ == '__main__':
    unittest.main()
