#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import unittest


def word_weight(s: str, n: int) -> int:
    # write your solution here
    str2int = ''.join([str(string.ascii_lowercase.index(c) + 1) for c in s])

    result = 0
    for _ in range(n):
        result = 0
        for c in str2int:
            result += int(c)

        str2int = str(result)

    return result


class TestWordWeight(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(20, string.ascii_lowercase.index("t") + 1)
        self.assertEqual("2021189147", ''.join([str(string.ascii_lowercase.index(c) + 1) for c in "turing"]))

        self.assertEqual(35, word_weight("turing", 1))
        self.assertEqual(8, word_weight("turing", 2))

    def testBasic1(self):
        self.assertEqual(28, word_weight("turin", 1))
        self.assertEqual(10, word_weight("turin", 2))


if __name__ == '__main__':
    unittest.main()
