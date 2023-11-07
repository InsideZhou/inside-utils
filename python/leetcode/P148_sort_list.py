#!/usr/bin/env python
# https://leetcode.cn/problems/sort-list/
from __future__ import annotations
import random
import unittest
from typing import Optional

from leetcode.P92_reverse_linked_list_ii import ListNode, ListNodePointer
from leetcode.P98_validate_binary_search_tree import BinarySearchTreeNode


# 利用二叉搜索树排序，如果建立的树近似于单链表，就失去了二叉树的优势，不适合在已经近乎有序的数据集上使用。
def bst_sort(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    elif head.next is None:
        return head

    tree = BinarySearchTreeNode(head.val)

    while head.next is not None:
        tree.add(head.next.val)
        head = head.next

    tree_nodes = tree.inorder_traversal()
    list_nodes = []
    for i in range(len(tree_nodes) - 1, -1, -1):
        tn = tree_nodes[i]

        for _ in range(tn.weight):
            first_list_node = list_nodes[-1] if len(list_nodes) > 0 else None
            list_nodes.append(ListNode(tn.val, first_list_node))

    return list_nodes[-1] if len(list_nodes) > 0 else None


def insertion_sort(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    elif head.next is None:
        return head

    sorted_boundary = head
    cursor_pointer = ListNodePointer(head)
    cursor_pointer.move_forward()

    while cursor_pointer.current is not None:
        current = cursor_pointer.current

        if current.val > sorted_boundary.val and sorted_boundary.next is current:
            sorted_boundary = sorted_boundary.next
            cursor_pointer.move_forward()
            continue

        current = cursor_pointer.bypass()

        if current.val > sorted_boundary.val:
            sorted_boundary.append(current)
            sorted_boundary = sorted_boundary.next
        elif current.val <= head.val:
            current.next = head
            head = current
            cursor_pointer.position += 1
        else:
            insert_pointer = ListNodePointer(head)

            while current.val > insert_pointer.current.val:
                insert_pointer.move_forward()

            insert_pointer.insert(current)
            cursor_pointer.position += 1

    return head


def quick_sort(head: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
    if head is None:
        return None, None
    elif head.next is None:
        return head, head
    elif head.next.next is None:
        if head.val <= head.next.val:
            former = head
            latter = head.next
        else:
            former = head.next
            latter = head

        former.next = latter
        latter.next = None
        return former, latter

    pivot_val = head.val

    left_head = None
    left_end = None
    pivot_head = None
    pivot_end = None
    right_head = None
    right_end = None

    cursor_pointer = ListNodePointer(head)
    while cursor_pointer.current is not None:
        current = cursor_pointer.bypass()
        current.next = None

        if current.val < pivot_val:
            if left_end is None:
                left_head = current
                left_end = current
            else:
                left_end.next = current
                left_end = left_end.next
        elif current.val == pivot_val:
            if pivot_end is None:
                pivot_head = current
                pivot_end = current
            else:
                pivot_end.next = current
                pivot_end = pivot_end.next
        else:
            if right_head is None:
                right_head = current
                right_end = current
            else:
                right_end.next = current
                right_end = right_end.next

    left_head, left_end = quick_sort(left_head)
    right_head, right_end = quick_sort(right_head)

    if left_head is not None:
        head = left_head
        left_end.next = pivot_head
    else:
        head = pivot_head

    if right_head is not None:
        pivot_end.next = right_head
        end = right_end
    else:
        end = pivot_end

    return head, end


# noinspection PyCompatibility
def merge_sort(head: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
    if head is None:
        return None
    elif head.next is None:
        return head

    turn_index = 0
    booth_length = pow(2, turn_index)
    group_length = booth_length * 2

    cursor_index = 0
    cursor = head

    group_end: Optional[ListNode] = None

    former_booths_head: Optional[ListNode] = None
    former_booths_end: Optional[ListNode] = None

    latter_booths_head: Optional[ListNode] = None
    latter_booths_end: Optional[ListNode] = None

    while True:
        current = cursor
        booth_index = cursor_index % group_length
        if 0 == booth_index:
            former_booths_head = current
            former_booths_end = current
        elif 0 < booth_index < booth_length:
            former_booths_end.next = current
            former_booths_end = former_booths_end.next
        elif booth_index == booth_length:
            latter_booths_head = current
            latter_booths_end = current
        else:
            latter_booths_end.next = current
            latter_booths_end = latter_booths_end.next

        cursor = cursor.next
        cursor_index += 1

        if booth_index == group_length - 1 or cursor is None:
            former_booths_end.next = None
            if latter_booths_end is not None:
                latter_booths_end.next = None

            prev_group_end = group_end
            group_head, group_end = merge(former_booths_head, latter_booths_head)

            if prev_group_end is not None:
                prev_group_end.next = group_head

            if cursor_index <= group_length:
                head = group_head

            former_booths_head = None
            former_booths_end = None
            latter_booths_head = None
            latter_booths_end = None

        if cursor is None:
            if cursor_index <= group_length:
                break

            # start next turn
            turn_index += 1
            booth_length = pow(2, turn_index)
            group_length = booth_length * 2

            cursor_index = 0
            cursor = head

            former_booths_head = None
            former_booths_end = None
            latter_booths_head = None
            latter_booths_end = None
            group_end = None

    if group_end is not None:
        group_end.next = None

    return head, group_end


def merge(left_node: Optional[ListNode], right_node: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
    head = ListNode()
    tail = head

    while left_node is not None or right_node is not None:
        if left_node is None:
            current = right_node
            right_node = right_node.next
        elif right_node is None:
            current = left_node
            left_node = left_node.next
        elif left_node.val <= right_node.val:
            current = left_node
            left_node = left_node.next
        else:
            current = right_node
            right_node = right_node.next

        current.next = None
        tail.next = current
        tail = current

    head = head.next
    return head, tail


# noinspection DuplicatedCode
class TestReverseLinkedListII(unittest.TestCase):
    def testSimple(self):
        a = ListNode(1)
        b = ListNode(2, a)

        head = insertion_sort(b)
        sorted_list = []
        while head is not None:
            sorted_list.append(head.val)
            head = head.next

        self.assertEqual([1, 2], sorted_list)

    def testBasic(self):
        a = ListNode(3)
        b = ListNode(1, a)
        c = ListNode(2, b)
        d = ListNode(4, c)

        head = insertion_sort(d)
        sorted_list = []
        while head is not None:
            sorted_list.append(head.val)
            head = head.next

        self.assertEqual([1, 2, 3, 4], sorted_list)

    def testStandard(self):
        a = ListNode(0)
        b = ListNode(4, a)
        c = ListNode(3, b)
        d = ListNode(5, c)
        e = ListNode(-1, d)

        head = insertion_sort(e)
        sorted_list = []
        while head is not None:
            sorted_list.append(head.val)
            head = head.next

        self.assertEqual([-1, 0, 3, 4, 5], sorted_list)

    def testDuplicateNodes(self):
        a = ListNode(15)
        b = ListNode(11, a)
        c = ListNode(5, b)
        d = ListNode(8, c)
        e = ListNode(1, d)
        f = ListNode(-3, e)
        g = ListNode(5, f)
        h = ListNode(14, g)
        i = ListNode(19, h)
        j = ListNode(4, i)

        head = bst_sort(j)
        sorted_list = []
        while head is not None:
            sorted_list.append(head.val)
            head = head.next

        self.assertEqual([-3, 1, 4, 5, 5, 8, 11, 14, 15, 19], sorted_list)

    def testNearlySortedList(self):
        value_list = list(range(1, 50000)) + [0]

        nodes = []
        for i in reversed(value_list):
            n = ListNode(i, nodes[-1]) if len(nodes) > 0 else ListNode(i)
            nodes.append(n)

        head, _ = merge_sort(nodes[-1])
        sorted_list = []
        while head is not None:
            sorted_list.append(head.val)
            head = head.next

        self.assertEqual(list(range(50000)), sorted_list)

    def testBigList(self):
        value_list = list(range(50000))
        random.shuffle(value_list)

        nodes = []
        for i in reversed(value_list):
            n = ListNode(i, nodes[-1]) if len(nodes) > 0 else ListNode(i)
            nodes.append(n)

        head, _ = quick_sort(nodes[-1])
        sorted_list = []
        while head is not None:
            sorted_list.append(head.val)
            head = head.next

        self.assertEqual(list(range(50000)), sorted_list)


if __name__ == '__main__':
    unittest.main()
