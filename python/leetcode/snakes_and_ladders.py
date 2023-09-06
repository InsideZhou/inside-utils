#!/usr/bin/env python
# https://leetcode.cn/problems/snakes-and-ladders/
import unittest
from collections import deque
from typing import List


# noinspection PyShadowingBuiltins
def id_to_index(id: int, dimension: int) -> (int, int):
    """
    索引方向是从左到右、自上而下。
    """

    row = (id - 1) // dimension
    row = dimension - 1 - row  # 上下颠倒

    col = (id - 1) % dimension

    # 行数从0开始
    if dimension % 2 == 0:
        col = dimension - 1 - col if row % 2 == 0 else col  # 总行数是偶数时，偶数行倒序
    else:
        col = dimension - 1 - col if row % 2 == 1 else col  # 总行数是奇数时，奇数行倒序

    return row, col


# noinspection PyShadowingBuiltins
def board_val(board: List[List[int]], id: int) -> int:
    i, j = id_to_index(id, len(board))
    return board[i][j]


def snakes_and_ladders(board: List[List[int]]) -> int:
    dimension = len(board)
    max_stay_id = pow(dimension, 2)

    visited_stays = set()
    pending_stays = deque([(1, 0)])
    while len(pending_stays) > 0:
        stay_id, steps_count = pending_stays.popleft()

        if stay_id in visited_stays:
            continue
        else:
            visited_stays.add(stay_id)

        stays = []
        for step_length in range(6, 0, -1):  # 添加所有非-1的值，值为-1时，保留编号最大的。
            next_stay_id = stay_id + step_length
            if next_stay_id >= max_stay_id:
                return steps_count + 1

            i, j = id_to_index(next_stay_id, dimension)
            stay_val = board[i][j]

            if -1 != stay_val:
                next_stay_id = stay_val
                stays.append(next_stay_id)
            elif -1 not in stays:
                stays.append(-1)
                stays.append(next_stay_id)

            if next_stay_id == max_stay_id:
                return steps_count + 1

        pending_stays.extend([(s, steps_count + 1) for s in stays if s != -1])

    return -1


class TestSnakesAndLadders(unittest.TestCase):
    def testIdToIndex(self):
        self.assertEqual((0, 0), id_to_index(36, 6))
        self.assertEqual((0, 5), id_to_index(31, 6))
        self.assertEqual((5, 0), id_to_index(1, 6))
        self.assertEqual((5, 5), id_to_index(6, 6))

        self.assertEqual((2, 2), id_to_index(22, 6))
        self.assertEqual((2, 3), id_to_index(21, 6))
        self.assertEqual((3, 2), id_to_index(15, 6))
        self.assertEqual((3, 3), id_to_index(16, 6))

        self.assertEqual((0, 0), id_to_index(7, 3))
        self.assertEqual((0, 2), id_to_index(9, 3))
        self.assertEqual((1, 1), id_to_index(5, 3))
        self.assertEqual((2, 0), id_to_index(1, 3))
        self.assertEqual((2, 1), id_to_index(2, 3))
        self.assertEqual((2, 2), id_to_index(3, 3))

        self.assertEqual((0, 0), id_to_index(16, 4))
        self.assertEqual((0, 3), id_to_index(13, 4))
        self.assertEqual((3, 0), id_to_index(1, 4))
        self.assertEqual((3, 2), id_to_index(3, 4))
        self.assertEqual((3, 3), id_to_index(4, 4))

        self.assertEqual((0, 0), id_to_index(21, 5))
        self.assertEqual((0, 4), id_to_index(25, 5))
        self.assertEqual((2, 2), id_to_index(13, 5))
        self.assertEqual((3, 0), id_to_index(10, 5))
        self.assertEqual((3, 4), id_to_index(6, 5))
        self.assertEqual((4, 0), id_to_index(1, 5))
        self.assertEqual((4, 4), id_to_index(5, 5))

    def testSimple(self):
        self.assertEqual(1, snakes_and_ladders([[-1, -1], [-1, 3]]))

    def testN3Circle(self):
        self.assertEqual(1, snakes_and_ladders([
            [-1, -1, -1],
            [-1, 9, 8],
            [-1, 8, 9]]))

    def testN3(self):
        self.assertEqual(-1, snakes_and_ladders([
            [1, 1, -1],
            [1, 1, 1],
            [-1, 1, 1]]))

    def testN4(self):
        self.assertEqual(1, snakes_and_ladders([
            [-1, -1, 2, -1],
            [14, 2, 12, 3],
            [4, 9, 1, 11],
            [-1, 2, 1, 16]]))

    def testN4_1(self):
        self.assertEqual(2, snakes_and_ladders([
            [-1, 1, 2, -1],
            [2, 13, 15, -1],
            [-1, 10, -1, -1],
            [-1, 6, 2, 8]]))

    def testN5(self):
        self.assertEqual(2, snakes_and_ladders([
            [-1, -1, 19, 10, -1],
            [2, -1, -1, 6, -1],
            [-1, 17, -1, 19, -1],
            [25, -1, 20, -1, -1],
            [-1, -1, -1, -1, 15]]))

    def testN5_1(self):
        self.assertEqual(3, snakes_and_ladders([
            [-1, 10, -1, 15, -1],
            [-1, -1, 18, 2, 20],
            [-1, -1, 12, -1, -1],
            [2, 4, 11, 18, 8],
            [-1, -1, -1, -1, -1]]))

    def testN6(self):
        self.assertEqual(4, snakes_and_ladders([
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1]]))

    def testN7(self):
        self.assertEqual(3, snakes_and_ladders([
            [-1, 5, -1, -1, 17, 6, -1],
            [41, 28, -1, -1, -1, 27, -1],
            [35, 42, -1, -1, -1, -1, 4],
            [7, 32, -1, 25, -1, 43, -1],
            [-1, 26, 5, -1, -1, -1, 25],
            [28, -1, -1, 5, -1, -1, 41],
            [-1, 42, 28, 25, -1, 7, 28]]))

    def testN12(self):
        self.assertEqual(5, snakes_and_ladders([
            [-1, -1, -1, -1, 33, -1, -1, -1, -1, 37, -1, -1],
            [-1, -1, -1, 17, 128, 113, 11, 5, -1, 99, -1, -1],
            [10, -1, 72, 112, 72, 31, -1, -1, 62, -1, -1, -1],
            [-1, -1, -1, -1, -1, 6, 21, 122, -1, 1, -1, 39],
            [-1, -1, -1, -1, -1, -1, -1, 79, -1, 128, 81, -1],
            [-1, 16, -1, 120, -1, -1, 11, 62, -1, -1, -1, -1],
            [101, 88, 87, -1, -1, -1, -1, -1, -1, -1, -1, 40],
            [-1, -1, 90, 80, -1, -1, -1, -1, -1, -1, -1, 35],
            [-1, 78, -1, -1, -1, 62, -1, -1, -1, -1, -1, -1],
            [-1, 3, -1, -1, -1, -1, -1, -1, 89, -1, -1, -1],
            [-1, 44, -1, -1, -1, 103, 134, -1, 69, -1, -1, 123],
            [-1, 24, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]))

    def testN12_1(self):
        self.assertEqual(5, snakes_and_ladders([
            [-1, 48, -1, -1, -1, 10, -1, -1, 35, -1, 141, -1],
            [-1, 128, -1, -1, 68, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, 36, -1, -1, -1, -1, -1, 80, -1, 98, -1],
            [-1, -1, -1, -1, 122, 39, 122, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, 134, -1, -1, 59, -1],
            [116, -1, -1, 65, -1, -1, -1, -1, 129, -1, -1, 35],
            [-1, 61, 80, 1, -1, -1, -1, -1, -1, 81, -1, 7],
            [-1, -1, -1, 70, -1, -1, -1, -1, -1, 135, -1, -1],
            [-1, -1, -1, -1, -1, 59, 105, -1, 126, 44, -1, -1],
            [-1, -1, 1, -1, -1, -1, -1, 139, -1, -1, -1, -1],
            [98, 138, -1, -1, -1, 109, 111, 103, -1, -1, -1, -1],
            [-1, -1, -1, -1, 66, -1, -1, -1, -1, -1, -1, -1]]))

    def testN13(self):
        self.assertEqual(5, snakes_and_ladders([
            [-1, 51, -1, -1, -1, -1, 5, 132, -1, -1, -1, -1, -1],
            [-1, 122, -1, -1, -1, -1, 73, 110, 130, -1, 125, -1, -1],
            [-1, 105, -1, -1, 84, -1, -1, 131, -1, -1, -1, -1, -1],
            [-1, -1, -1, 128, 139, 131, -1, 4, 123, 35, -1, -1, -1],
            [-1, -1, -1, -1, -1, 38, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, 18, -1, -1, 169, 162, -1, -1, -1, -1, 95, 100],
            [16, -1, -1, -1, -1, -1, -1, -1, -1, -1, 34, -1, 80],
            [150, -1, -1, 127, 96, 105, -1, 55, 104, -1, -1, -1, -1],
            [-1, 1, -1, -1, 144, -1, -1, 114, -1, 106, -1, -1, -1],
            [-1, -1, -1, 31, -1, -1, 41, -1, 124, -1, -1, -1, 62],
            [-1, 8, -1, -1, -1, -1, 94, -1, 100, -1, -1, 76, -1],
            [-1, 45, -1, -1, -1, -1, -1, 64, -1, 4, 74, -1, 67],
            [-1, 40, -1, -1, -1, -1, -1, 64, -1, -1, -1, -1, -1]]))


if __name__ == '__main__':
    unittest.main()
