#!/usr/bin/env python
# https://leetcode.cn/problems/minimum-time-to-type-word-using-special-typewriter
import unittest
from string import ascii_lowercase

'''
本质上是求一个有限可循环数轴中两点的距离。
d(a,b)=min(∣a−b∣,R−L−∣a−b∣)
'''


def min_time_to_type_word(word):
    total_ticks, pointer, letter_count = 0, ascii_lowercase.index('a'), len(ascii_lowercase)

    for letter in word:
        target = ascii_lowercase.index(letter)
        abs_diff = abs(target - pointer)
        distance = min(abs_diff, letter_count - abs_diff)

        pointer = target

        total_ticks += distance  # move pointer
        total_ticks += 1  # type current letter

    return total_ticks


class TestMinimumTimeToTypeWordUsingSpecialTypewriter(unittest.TestCase):
    def testBasic1(self):
        self.assertEqual(1, min_time_to_type_word('a'))

    def testBasic2(self):
        self.assertEqual(5, min_time_to_type_word('abc'))

    def testBasic3(self):
        self.assertEqual(7, min_time_to_type_word('bza'))

    def testBasic4(self):
        self.assertEqual(34, min_time_to_type_word('zjpc'))


if __name__ == '__main__':
    unittest.main()
