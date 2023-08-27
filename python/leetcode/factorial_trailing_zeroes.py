#!/usr/bin/env python
# https://leetcode.cn/problems/factorial-trailing-zeroes/

import unittest


def trailing_zeroes(n: int) -> int:
    result = 0
    while n >= 5:
        n //= 5
        result += n

    return result


class TestTrailingZeroes(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(0, trailing_zeroes(3))
        self.assertEqual(1, trailing_zeroes(6))
        self.assertEqual(2, trailing_zeroes(11))
        self.assertEqual(6, trailing_zeroes(27))


if __name__ == '__main__':
    unittest.main()
