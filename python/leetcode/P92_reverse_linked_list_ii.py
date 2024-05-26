#!/usr/bin/env python
# https://leetcode.cn/problems/reverse-linked-list-ii/
from __future__ import annotations

import unittest
from typing import Optional, List, Generator


class ListNode:
    @staticmethod
    def construct_from_values(values: List[int]) -> ListNode:
        head = None
        node = None
        for val in values:
            if node is None:
                node = ListNode(val)
                head = node
            else:
                node.next = ListNode(val)
                node = node.next

        return head

    def __init__(self, val=0, next_node: ListNode = None):
        self.val = val
        self.next = next_node

    def swap(self, other_node: ListNode):
        self.next, other_node.next = other_node.next, self.next

    def append(self, other_node: ListNode):
        other_node.next = self.next
        self.next = other_node

    def connect(self, next_node: ListNode):
        self.next = next_node

    def to_values(self) -> Generator[int]:
        node = self
        while node is not None:
            yield node.val
            node = node.next

    def rotate_right(self, k: int) -> Optional[ListNode]:
        """
        必须拿到链表末元素的指针，才能完成rotate，而在此过程中，顺势计算链表长度，稍后可以借助模运算（k mod 链表长度n）来减少指针移动次数。
        """

        head = self

        if 0 == k:
            return head

        current = head
        count = 1

        while current.next is not None:
            current = current.next
            count += 1

        end = current
        cut = count - k % count - 1

        current = head
        index = 0
        while index < cut:
            current = current.next
            index += 1

        if current != end:
            end.next, head = head, current.next
            current.next = None

        return head


# noinspection PyCompatibility
class ListNodePointer:
    def __init__(self, head: Optional[ListNode], pointer: ListNodePointer = None):
        self.position = 0
        self.prev: Optional[ListNode] = None
        self.current: Optional[ListNode] = head
        self.next: Optional[ListNode] = head.next if head is not None else None

        if pointer is not None:
            self.position = pointer.position
            self.prev = pointer.prev
            self.current = pointer.current
            self.next = pointer.next

    def bypass(self) -> Optional[ListNode]:
        current = self.current
        if current is None:
            return None

        if self.prev is not None:
            self.prev.next = self.next

        self.current = self.next

        if self.next is not None:
            self.next = self.next.next

        return current

    def insert(self, node: ListNode):
        prev = self.prev

        if prev is not None:
            prev.next = node

        node.next = self.current
        self.prev = node
        self.position += 1

    def append(self, node: ListNode):
        node.next = self.next
        self.next = node
        self.current.next = node

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

    pointer = ListNodePointer(head)

    while pointer.current is not None:
        if first_break is not None and second_break is None:
            pointer.current.next = pointer.prev

        if pointer.position == left - 1:
            first_break = ListNodePointer(None, pointer)

        if pointer.position == right - 1:
            second_break = ListNodePointer(None, pointer)
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
