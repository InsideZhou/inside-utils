#!/usr/bin/env python
# https://leetcode.cn/problems/sort-list/
import random
import unittest
from typing import Optional, List

from maximum_binary_tree import TreeNode
from reverse_linked_list_ii import ListNode, ListNodePointer


# 利用二叉搜索树排序，如果建立的树近似于单链表，就失去了二叉树的优势，不适合在已经近乎有序的数据集上使用。
def bst_sort(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    elif head.next is None:
        return head

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


def quick_sort(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    elif head.next is None:
        return head

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


def merge_sort(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    elif head.next is None:
        return head

    cursor_pointer = ListNodePointer(head)
    cursor_pointer.current = head
    cursor_pointer.next = head.next

    mid_pointer = ListNodePointer(None, cursor_pointer)
    sorted_pointer = ListNodePointer(None, cursor_pointer)

    while cursor_pointer.current is not None:
        if mid_pointer.position < (cursor_pointer.position - sorted_pointer.position) // 2 + sorted_pointer.position:
            mid_pointer.move_forward()

        if sorted_pointer.next is not None and sorted_pointer.current.val < sorted_pointer.next.val:
            mid_pointer.move_forward()
            sorted_pointer.move_forward()

        cursor_pointer.move_forward()

    if sorted_pointer.position == cursor_pointer.position:
        return head

    cursor_head = mid_pointer.next
    mid_pointer.current.next = None

    if sorted_pointer.position == mid_pointer.position:
        merged_head = __merge(head, merge_sort(cursor_head))
        return merged_head

    mid_head = sorted_pointer.next
    sorted_pointer.current.next = None

    merged_head = __merge(head, __merge(merge_sort(mid_head), merge_sort(cursor_head)))
    return merged_head


def __merge(left_node: Optional[ListNode], right_node: Optional[ListNode]) -> Optional[ListNode]:
    if left_node is None:
        return right_node
    elif right_node is None:
        return left_node

    head = ListNode()
    tail = head

    left_pointer = ListNodePointer(left_node)
    right_pointer = ListNodePointer(right_node)

    while left_pointer.current is not None or right_pointer.current is not None:
        left = left_pointer.current
        right = right_pointer.current

        if left is None:
            current = right
            right_pointer.move_forward()
        elif right is None:
            current = left
            left_pointer.move_forward()
        elif left.val <= right.val:
            current = left
            left_pointer.move_forward()
        else:
            current = right
            right_pointer.move_forward()

        current.next = None
        tail.next = current
        tail = current

    head = head.next
    return head


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

        head = insertion_sort(j)
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

        head = insertion_sort(nodes[-1])
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

        head = quick_sort(nodes[-1])
        sorted_list = []
        while head is not None:
            sorted_list.append(head.val)
            head = head.next

        self.assertEqual(list(range(50000)), sorted_list)

    def testMergeSort(self):
        a = ListNode(1)
        b = ListNode(4, a)
        c = ListNode(9, b)
        d = ListNode(2, c)

        head = merge_sort(d)
        sorted_list = []
        while head is not None:
            sorted_list.append(head.val)
            head = head.next

        self.assertEqual([1, 2, 4, 9], sorted_list)


if __name__ == '__main__':
    unittest.main()
