#!/usr/bin/env python
# https://leetcode.cn/problems/reverse-linked-list-ii/
from __future__ import annotations

import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_node: ListNode=None):
        self.val = val
        self.next = next_node


# noinspection PyCompatibility
class ListNodePointer:
    def __init__(self, pointer: ListNodePointer = None):
        self.position = 0
        self.prev: Optional[ListNode] = None
        self.current: Optional[ListNode] = None
        self.next: Optional[ListNode] = None

        if pointer is not None:
            self.position = pointer.position
            self.prev = pointer.prev
            self.current = pointer.current
            self.next = pointer.next

    def move_forward(self):
        self.position += 1
        self.prev = self.current
        self.current = self.next

        if self.next is not None:
            self.next = self.next.next


# 使用自定义指针记录链表断开点，能让逻辑清晰许多，也更简洁。
# noinspection PyCompatibility
def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    first_break: Optional[ListNodePointer] = None
    second_break: Optional[ListNodePointer] = None

    pointer = ListNodePointer()
    pointer.position = 1
    pointer.prev = None
    pointer.current = head
    pointer.next = head.next

    while pointer.current is not None:
        if first_break is not None and second_break is None:
            pointer.current.next = pointer.prev

        if pointer.position == left:
            first_break = ListNodePointer(pointer)

        if pointer.position == right:
            second_break = ListNodePointer(pointer)
            break

        pointer.move_forward()

    if first_break is None:
        return None

    if second_break is None:
        return pointer.prev

    first_break.current.next = second_break.next

    if first_break.prev is None:
        return second_break.current

    first_break.prev.next = second_break.current

    return head


class TestReverseLinkedListII(unittest.TestCase):
    def test_basic(self):
        e = ListNode(5)
        c = ListNode(3, e)
        head = reverse_between(c, 1, 2)

        values = []
        while head is not None:
            values.append(head.val)
            head = head.next

        self.assertEqual([5, 3], values)

    def test_standard(self):
        e = ListNode(5)
        d = ListNode(4, e)
        c = ListNode(3, d)
        b = ListNode(2, c)
        a = ListNode(1, b)
        head = reverse_between(a, 2, 4)

        values = []
        while head is not None:
            values.append(head.val)
            head = head.next

        self.assertEqual([1, 4, 3, 2, 5], values)

    def test_simple(self):
        head = reverse_between(ListNode(5), 1, 1)
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next

        self.assertEqual([5], values)

    def test_simple2(self):
        e = ListNode(5)
        c = ListNode(3, e)
        head = reverse_between(c, 1, 1)

        values = []
        while head is not None:
            values.append(head.val)
            head = head.next

        self.assertEqual([3, 5], values)

    def test_to_end(self):
        e = ListNode(5)
        d = ListNode(4, e)
        c = ListNode(3, d)
        b = ListNode(2, c)
        a = ListNode(1, b)
        head = reverse_between(a, 2, 5)

        values = []
        while head is not None:
            values.append(head.val)
            head = head.next

        self.assertEqual([1, 5, 4, 3, 2], values)


if __name__ == '__main__':
    unittest.main()
