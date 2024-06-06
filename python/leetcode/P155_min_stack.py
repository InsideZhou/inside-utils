#!/usr/bin/env python
# https://leetcode.cn/problems/min-stack/
import unittest


# noinspection PyPep8Naming
class MinStack:
    """
    基本思路是，为一个集合建立另一个辅助集合，两个集合之间有严格的对应关系，这样就可以做到在集合中同一个位置，能有两个截然不同的值，因为另一个值由辅助集合提供。
    本题中，为主栈建立辅助栈，辅助栈中记录的是当前位置所对应的整栈最小值。
    """

    def __init__(self):
        self.__sorted_stack = []
        self.__stack = []

    def push(self, val: int) -> None:
        if self.__sorted_stack:
            self.__sorted_stack.append(val if self.__sorted_stack[-1] > val else self.__sorted_stack[-1])
        else:
            self.__sorted_stack.append(val)

        self.__stack.append(val)

    def pop(self) -> None:
        self.__sorted_stack.pop()
        self.__stack.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__sorted_stack[-1]


class TestMinStack(unittest.TestCase):
    def test_basic(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)

        self.assertEqual(-3, stack.getMin())

        stack.pop()
        self.assertEqual(0, stack.top())
        self.assertEqual(-2, stack.getMin())

    def test_min(self):
        stack = MinStack()
        stack.push(0)
        stack.push(1)
        stack.push(0)

        self.assertEqual(0, stack.getMin())
        stack.pop()
        self.assertEqual(0, stack.getMin())

    def test_top(self):
        stack = MinStack()
        stack.push(2147483646)
        stack.push(2147483646)
        stack.push(2147483647)

        self.assertEqual(2147483647, stack.top())
        stack.pop()
        self.assertEqual(2147483646, stack.getMin())
        stack.pop()
        self.assertEqual(2147483646, stack.getMin())
        stack.pop()

        stack.push(2147483647)
        self.assertEqual(2147483647, stack.top())
        self.assertEqual(2147483647, stack.getMin())

        stack.push(-2147483648)
        self.assertEqual(-2147483648, stack.top())
        self.assertEqual(-2147483648, stack.getMin())
        stack.pop()
        self.assertEqual(2147483647, stack.getMin())


if __name__ == '__main__':
    unittest.main()
