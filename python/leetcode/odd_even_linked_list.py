#!/usr/bin/env python
# https://leetcode.cn/problems/odd-even-linked-list/
import unittest
from typing import Optional

from leetcode.reverse_linked_list_ii import ListNode


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    tail = head
    even_head = head.next

    if even_head is not None:
        even_tail = even_head
        cursor = even_head.next
        even_tail.next = None
        tail.next = None
        index = 2

        while cursor is not None:
            current = cursor
            cursor = cursor.next
            current.next = None

            if index % 2 == 1:
                even_tail.next = current
                even_tail = current
            else:
                tail.next = current
                tail = current

            index += 1

    tail.next = even_head
    return head


class TestOddEvenLinkedList(unittest.TestCase):
    def testBasic(self):
        l = ListNode.construct_from_values([1, 2, 3, 4, 5])
        l = odd_even_list(l)
        self.assertEqual([1, 3, 5, 2, 4], list(l.to_values()))

    def testStandard(self):
        l = ListNode.construct_from_values([2, 1, 3, 5, 6, 4, 7])
        l = odd_even_list(l)
        self.assertEqual([2, 3, 6, 7, 1, 5, 4], list(l.to_values()))


if __name__ == '__main__':
    unittest.main()
