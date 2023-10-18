#!/usr/bin/env python
# https://leetcode.cn/problems/merge-strings-alternately/
import unittest


def merge_alternately(word1: str, word2: str) -> str:
    result = []
    for i in range(max(len(word1), len(word2))):
        result.append(word1[i:i + 1])
        result.append(word2[i:i + 1])

    return ''.join(result)


class TestMergeStringsAlternately(unittest.TestCase):
    def testBasic(self):
        self.assertEqual("apbqcr", merge_alternately("abc", "pqr"))
        self.assertEqual("apbqcrs", merge_alternately("abc", "pqrs"))
        self.assertEqual("apbqcd", merge_alternately("abcd", "pq"))


if __name__ == '__main__':
    unittest.main()
