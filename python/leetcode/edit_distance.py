#!/usr/bin/env python
# https://leetcode.cn/problems/edit-distance/
import numpy, unittest
from collections import deque
from typing import List


def min_distance(base_word1: str, base_word2: str) -> int:
    """
    本算法思路的基础是：要从A字符串以最少的步骤改成B字符串，则需要按相同字母对齐俩字符串，对齐字母数量越多的方案，则需要的修改量越少。
    """

    base_word1_length = len(base_word1)
    base_word2_length = len(base_word2)

    if base_word1 == '':
        return base_word2_length
    elif base_word2 == '':
        return base_word1_length

    def align(op1: str, op2: str):
        op1_length, op2_length = len(op1), len(op2)
        idx1, idx2 = 0, 0
        while idx1 < op1_length:
            idx2 = 0
            while idx2 < op2_length:
                if op1[idx1] == op2[idx2]:
                    yield [idx1, idx2]
                idx2 += 1
            idx1 += 1

    def split(op1: str, op2: str, idx1_start: int, idx2_start: int) -> (int, int, int, int):
        op1_length, op2_length = len(op1), len(op2)

        idx1_stop, idx2_stop = idx1_start + 1, idx2_start + 1
        while idx1_stop < op1_length and idx2_stop < op2_length and op1[idx1_stop] == op2[idx2_stop]:
            idx1_stop += 1
            idx2_stop += 1

        return idx1_start, idx1_stop, idx2_start, idx2_stop, max(op1_length, op2_length)

    group_id_generator = 0
    distance = max(base_word1_length, base_word2_length)
    new_queue, queue = deque([(group_id_generator, distance, deque([(base_word1, base_word2)]))]), deque()

    while len(new_queue) > 0:
        new_queue, queue = queue, new_queue
        while True:
            try:
                group_id, group_distance, word_groups = queue.popleft()
            except IndexError:
                break

            if group_distance > distance:
                continue
            distance = group_distance

            try:
                w1, w2 = word_groups.popleft()
            except IndexError:
                continue

            for group in align(w1, w2):
                split_result = split(w1, w2, group[0], group[1])
                pre1, pre2 = w1[0:split_result[0]], w2[0:split_result[2]]
                post1, post2 = w1[split_result[1]:], w2[split_result[3]:]
                new_word_groups = list(word_groups)[:]

                if pre1 != "" or pre2 != "":
                    new_word_groups.append((pre1, pre2))

                if post1 != "" or post2 != "":
                    new_word_groups.append((post1, post2))

                a_distance = max(len(pre1), len(pre2)) + max(len(post1), len(post2))

                if 0 == group_id:
                    group_id_generator += 1
                    queue_item = (
                        group_id_generator,
                        group_distance - (split_result[4] - a_distance),
                        deque(new_word_groups)
                    )
                else:
                    queue_item = (
                        group_id,
                        group_distance - (split_result[4] - a_distance),
                        deque(new_word_groups)
                    )

                new_queue.append(queue_item)
            else:
                new_queue.append((
                    group_id,
                    group_distance,
                    word_groups
                ))

    return distance


def min_distance_matrix(base_word1: str, base_word2: str) -> List[List[int]]:
    """
    动态规划
    """
    base_word1_length = len(base_word1)
    base_word2_length = len(base_word2)

    matrix_rows = base_word1_length + 1
    matrix_cols = base_word2_length + 1
    matrix = [[0] * matrix_cols for _ in range(matrix_rows)]

    if base_word1 == '' or base_word2 == '':
        return matrix

    matrix[0][0] = 0 if base_word1[0] == base_word2[0] else 1

    for r in range(matrix_rows):
        matrix[r][0] = r

    for c in range(matrix_cols):
        matrix[0][c] = c

    for r in range(1, matrix_rows):
        for c in range(1, matrix_cols):
            matrix[r][c] = min(matrix[r][c - 1] + 1,
                               matrix[r - 1][c] + 1,
                               matrix[r - 1][c - 1] \
                                   if base_word1[r - 1] == base_word2[c - 1] \
                                   else matrix[r - 1][c - 1] + 1)

    return matrix


def min_distance_dp(base_word1: str, base_word2: str) -> int:
    base_word1_length = len(base_word1)
    base_word2_length = len(base_word2)

    if base_word1 == '':
        return base_word2_length
    elif base_word2 == '':
        return base_word1_length

    return min_distance_matrix(base_word1, base_word2)[base_word1_length][base_word2_length]


def print_matrix(array):
    print(numpy.asmatrix(numpy.array(array)))


class TestStringCompression(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(2, min_distance("se", "os"))
        self.assertEqual(2, min_distance_dp("se", "os"))

    def testSimple(self):
        self.assertEqual(3, min_distance("horse", "ros"))
        self.assertEqual(3, min_distance_dp("horse", "ros"))

    def testAllSame(self):
        self.assertEqual(0, min_distance("archlinux", "archlinux"))
        self.assertEqual(0, min_distance_dp("archlinux", "archlinux"))

    def testMidSame(self):
        self.assertEqual(8, min_distance("intentionosx", "executionwin"))
        self.assertEqual(8, min_distance_dp("intentionosx", "executionwin"))

    def testTailSame(self):
        self.assertEqual(5, min_distance("intention", "execution"))
        self.assertEqual(5, min_distance_dp("intention", "execution"))

    def testHeadSame(self):
        self.assertEqual(5, min_distance("noitnetni", "noitucexe"))
        self.assertEqual(5, min_distance_dp("noitnetni", "noitucexe"))

    def testAlmostDiff(self):
        self.assertEqual(5, min_distance("apple", "egg"))
        self.assertEqual(5, min_distance_dp("apple", "egg"))

    def testMidDiff(self):
        self.assertEqual(3, min_distance("teacher", "teerer"))
        self.assertEqual(3, min_distance_dp("teacher", "teerer"))

    def testMidSame1(self):
        self.assertEqual(27, min_distance("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically"))
        self.assertEqual(27, min_distance_dp("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically"))

    def testSameSequence(self):
        self.assertEqual(2, min_distance_dp("puu", "u"))


if __name__ == '__main__':
    unittest.main()
