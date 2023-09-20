#!/usr/bin/env python
# https://leetcode.cn/problems/string-compression/
import unittest
from typing import List


def compress(chars: List[str]) -> int:
    consecutively_char = chars[0]
    consecutively_char_count = 0
    chars.append('')
    while True:
        c = chars[0]
        del chars[0]

        if c != consecutively_char:
            chars.append(consecutively_char)
            if consecutively_char_count > 1:
                for i in str(consecutively_char_count):
                    chars.append(i)

            consecutively_char = c
            consecutively_char_count = 1
        else:
            consecutively_char_count += 1

        if '' == c:
            break

    return len(chars)


class TestStringCompression(unittest.TestCase):
    def testBasic(self):
        input_chars = ["a", "a", "b", "b", "c", "c", "c"]
        self.assertEqual(6, compress(input_chars))
        self.assertEqual(["a", "2", "b", "2", "c", "3"], input_chars)

    def testGroupGT10(self):
        input_chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        self.assertEqual(4, compress(input_chars))
        self.assertEqual(["a", "b", "1", "2"], input_chars)


if __name__ == '__main__':
    unittest.main()
