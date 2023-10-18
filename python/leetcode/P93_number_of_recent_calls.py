#!/usr/bin/env python
# https://leetcode.cn/problems/number-of-recent-calls/
import unittest

from collections import deque


class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while len(self.queue) > 0:
            if t - self.queue[0] > 3000:
                self.queue.popleft()
            else:
                break

        self.queue.append(t)
        return len(self.queue)


class TestNumberOfRecentCalls(unittest.TestCase):
    def testBasic(self):
        counter = RecentCounter()

        self.assertEqual(1, counter.ping(1))
        self.assertEqual(2, counter.ping(100))
        self.assertEqual(3, counter.ping(3001))
        self.assertEqual(3, counter.ping(3002))


if __name__ == '__main__':
    unittest.main()
