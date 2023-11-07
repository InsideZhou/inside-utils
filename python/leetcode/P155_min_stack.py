#!/usr/bin/env python
# https://leetcode.cn/problems/min-stack/
import unittest


class MinStack:
    def __init__(self):
        self.__min_value = None
        self.__stack = []

    def push(self, val: int) -> None:
        self.__min_value = val if self.__min_value is None else min(self.__min_value, val)
        self.__stack.append(val)

    def pop(self) -> int:
        val = self.__stack.pop()

        if len(self.__stack) == 0:
            self.__min_value = None
        else:
            self.__min_value = min(self.__stack)

        return val

    def top(self) -> int:
        return self.__stack[-1]

    def get_min(self) -> int:
        return self.__min_value


class TestMinStack(unittest.TestCase):
    def test_basic(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)

        self.assertEqual(-3, stack.get_min())

        stack.pop()
        self.assertEqual(0, stack.top())
        self.assertEqual(-2, stack.get_min())

    def test_min(self):
        stack = MinStack()
        stack.push(0)
        stack.push(1)
        stack.push(0)

        self.assertEqual(0, stack.get_min())
        stack.pop()
        self.assertEqual(0, stack.get_min())

    def test_top(self):
        stack = MinStack()
        stack.push(2147483646)
        stack.push(2147483646)
        stack.push(2147483647)

        self.assertEqual(2147483647, stack.top())
        stack.pop()
        self.assertEqual(2147483646, stack.get_min())
        stack.pop()
        self.assertEqual(2147483646, stack.get_min())
        stack.pop()

        stack.push(2147483647)
        self.assertEqual(2147483647, stack.top())
        self.assertEqual(2147483647, stack.get_min())

        stack.push(-2147483648)
        self.assertEqual(-2147483648, stack.top())
        self.assertEqual(-2147483648, stack.get_min())
        stack.pop()
        self.assertEqual(2147483647, stack.get_min())


if __name__ == '__main__':
    unittest.main()
