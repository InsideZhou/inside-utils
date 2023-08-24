#!/usr/bin/env python
# https://leetcode.cn/problems/valid-palindrome/
import string
import unittest

valid_chars = string.ascii_letters + string.digits


def is_palindrome(s: str) -> bool:
    normalized_str = ''.join([item for item in s if item in valid_chars])
    reversed_and_normalized_str = normalized_str[::-1]

    return normalized_str.lower() == reversed_and_normalized_str.lower()


class TestValidatePalindrome(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))


if __name__ == '__main__':
    unittest.main()
