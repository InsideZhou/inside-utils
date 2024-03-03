#!/usr/bin/env python
# https://leetcode.cn/problems/rotate-list
import unittest

from leetcode.P92_reverse_linked_list_ii import ListNode


class TestRotateList(unittest.TestCase):
    def testBasic(self):
        self.assertEqual([4, 5, 1, 2, 3],
                         list(ListNode.construct_from_values([1, 2, 3, 4, 5]).rotate_right(2).to_values()))

    def testBasic1(self):
        self.assertEqual([2, 0, 1], list(ListNode.construct_from_values([0, 1, 2]).rotate_right(4).to_values()))

    def testBasic2(self):
        self.assertEqual([1, 2], list(ListNode.construct_from_values([1, 2]).rotate_right(0).to_values()))

    def testBasic3(self):
        self.assertEqual([2, 1], list(ListNode.construct_from_values([1, 2]).rotate_right(1).to_values()))


if __name__ == '__main__':
    unittest.main()
