#!/usr/bin/env python
# https://leetcode.cn/problems/sort-list/
import random
import unittest
from typing import Optional, List

from maximum_binary_tree import TreeNode
from reverse_linked_list_ii import ListNode, ListNodePointer


# binary search tree sort
def bst_sort(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    tree = TreeNode(head.val)

    while head.next is not None:
        tree.bst_add(head.next.val)
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

    cursor = ListNodePointer()
    cursor.current = head
    cursor.next = head.next

    mid_pointer = ListNodePointer(cursor)

    while cursor.current is not None:
        if cursor.position / 2 > mid_pointer.position:
            mid_pointer.move_forward()

        prev_node = cursor.prev
        current_node = cursor.current
        next_node = cursor.next
        cursor.move_forward()

        if prev_node is not None and current_node.val < prev_node.val:
            prev_node.next = next_node
            cursor.prev = prev_node
            cursor.current = next_node
            if next_node is not None:
                cursor.next = next_node.next

            if current_node.val > mid_pointer.current.val:
                insert_pointer = ListNodePointer(mid_pointer)
            else:
                insert_pointer = ListNodePointer()
                insert_pointer.current = head
                insert_pointer.next = head.next

            while current_node.val > insert_pointer.current.val:
                insert_pointer.move_forward()

            prev_insert_node = insert_pointer.prev
            next_insert_node = insert_pointer.current

            current_node.next = next_insert_node
            if prev_insert_node is not None:
                prev_insert_node.next = current_node
            else:
                head = current_node

            mid_pointer = ListNodePointer(insert_pointer)
            mid_pointer.position += 1
            mid_pointer.prev = prev_insert_node
            mid_pointer.current = current_node
            mid_pointer.next = next_insert_node

    return head


def insertion_bst_sort(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    cursor = ListNodePointer()
    cursor.current = head
    cursor.next = head.next

    mid_pointer = ListNodePointer(cursor)

    while cursor.current is not None:
        if cursor.position - mid_pointer.position > 2 and cursor.position / 2 > mid_pointer.position:
            mid_pointer.move_forward()

        current_prev_node = cursor.prev
        current_node = cursor.current
        current_next_node = cursor.next
        cursor.move_forward()

        insertion_prev_node = mid_pointer.prev
        insertion_node = mid_pointer.current

        if current_node.val <= insertion_node.val and insertion_node != current_node:
            current_prev_node.next = current_next_node
            cursor.prev = current_prev_node

            current_node.next = insertion_node
            if insertion_prev_node is not None:
                insertion_prev_node.next = current_node
            else:
                head = current_node

            mid_pointer.position += 1
            mid_pointer.prev = insertion_prev_node
            mid_pointer.current = current_node
            mid_pointer.next = insertion_node

    mid_pointer.move_forward()
    mid_prev_node = mid_pointer.prev
    if mid_prev_node is not None:
        mid_node = mid_pointer.current
        mid_next_node = mid_pointer.next

        mid_prev_node.next = mid_next_node
        mid_node.next = head
        head = mid_node

    return bst_sort(head)


def quick_sort(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    nodes = []
    while head is not None:
        nodes.append(head)
        head = head.next

    nodes = __qsort(nodes)
    return nodes[0]


def __qsort(nodes: List[ListNode]) -> List[ListNode]:
    if 1 == len(nodes):
        return nodes

    pivot = nodes[random.randint(0, len(nodes) - 1)]
    pivot_region = []
    left_region = []
    right_region = []

    for current in nodes:
        if current.val > pivot.val:
            region = right_region
        elif current.val < pivot.val:
            region = left_region
        else:
            region = pivot_region
            if len(region) > 0:
                region[-1].next = current

        region.append(current)

    if len(left_region) > 0:
        left_region = __qsort(left_region)
        left_region[-1].next = pivot_region[0]
    else:
        left_region = []

    if len(right_region) > 0:
        right_region = __qsort(right_region)
        pivot_region[-1].next = right_region[0]
        right_region[-1].next = None
    else:
        right_region = []

    nodes = left_region + pivot_region + right_region
    nodes[-1].next = None
    return nodes


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

        head = quick_sort(j)
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

        head = quick_sort(nodes[-1])
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

        head = insertion_bst_sort(nodes[-1])
        sorted_list = []
        while head is not None:
            sorted_list.append(head.val)
            head = head.next

        self.assertEqual(list(range(50000)), sorted_list)


if __name__ == '__main__':
    unittest.main()
