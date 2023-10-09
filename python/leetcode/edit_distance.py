#!/usr/bin/env python
# https://leetcode.cn/problems/edit-distance/
import unittest
from collections import deque


def min_distance(base_word1: str, base_word2: str) -> int:
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


class TestStringCompression(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(2, min_distance("se", "os"))

    def testSimple(self):
        self.assertEqual(3, min_distance("horse", "ros"))

    def testAllSame(self):
        self.assertEqual(0, min_distance("archlinux", "archlinux"))

    def testMidSame(self):
        self.assertEqual(8, min_distance("intentionosx", "executionwin"))

    def testTailSame(self):
        self.assertEqual(5, min_distance("intention", "execution"))

    def testHeadSame(self):
        self.assertEqual(5, min_distance("noitnetni", "noitucexe"))

    def testAlmostDiff(self):
        self.assertEqual(5, min_distance("apple", "egg"))

    def testMidDiff(self):
        self.assertEqual(3, min_distance("teacher", "teerer"))

    def testeMidSame1(self):
        self.assertEqual(27, min_distance("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically"))


if __name__ == '__main__':
    unittest.main()
