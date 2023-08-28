#!/usr/bin/env python

import string
import unittest


# show me bug的题目之一。
def password_check(password: str) -> str:
    if not (8 <= len(password) <= 22):
        return "weak"

    lower_case_exists = False
    upper_case_exists = False
    digit_exists = False

    consecutively_char = ''
    consecutively_char_count = 0
    consecutively_char_limit = 3

    for c in password:
        if consecutively_char_count < consecutively_char_limit:
            if c == consecutively_char:
                consecutively_char_count += 1
            else:
                consecutively_char = c
                consecutively_char_count = 1

        if c in string.ascii_uppercase:
            upper_case_exists = True
        elif c in string.ascii_lowercase:
            lower_case_exists = True
        elif c in string.digits:
            digit_exists = True

    if consecutively_char_count >= consecutively_char_limit:
        return "weak"

    if not (lower_case_exists and upper_case_exists and digit_exists):
        return "weak"

    return "strong"


class TestPasswordCheck(unittest.TestCase):
    def testStrong(self):
        self.assertEqual("strong", password_check("1234567890Abcd"))

    def testRepeat(self):
        self.assertEqual("weak", password_check("1234567890aaaa"))

    def testNotEnough(self):
        self.assertEqual("weak", password_check("1234567890abcd"))


if __name__ == '__main__':
    unittest.main()
