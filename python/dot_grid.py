#!/usr/bin/env python

"""
Given a 3x3 dot grid on an Android lock screen:

. . .
. . .
. . .

1 2 3
4 5 6
7 8 9

Possible patterns:
1-2-5-8 = yes
1-2-3 = no
1-2-5-2 = no
8-5-2-1 = yes
1-2-3-9 = no
1-2-3-5 = yes
1-2-3-6-5-4 = yes

A password pattern is valid if (must satisfy all 4 conditions):
    1. The pattern passes through at least 4 dots on the grid
2. The next dot to connect to must be adjacent or diagonal to the current dot
    (no jumping to farther dots or out of bounds)
3. A valid pattern cannot have two of the same dot
4. A pattern is directional: back and forth on the same path are two distinct patterns

Compute the number of valid patterns and print the number.
"""
from __future__ import annotations

import unittest
from typing import List, Optional


# noinspection PyCompatibility
class DotGrid:
    def __init__(self, dots_count: int = 9):
        self.dots: List[Optional[Dot]] = [None] * dots_count

        for i in range(dots_count):
            self.dots[i] = Dot(i + 1)

        self.edges = []

    def connect(self, left_value: int, right_value: int) -> Edge:
        l_index = left_value - 1
        r_index = right_value - 1
        l_dot = self.dots[l_index]
        r_dot = self.dots[r_index]

        edge = next((e for e in l_dot.edges if e.left == r_index or e.right == r_index), None)
        if edge is not None:
            return edge

        edge = Edge(l_index, r_index)
        self.edges.append(edge)

        l_dot.adjacency_dots.append(r_index)
        l_dot.edges.append(edge)
        r_dot.adjacency_dots.append(l_index)
        r_dot.edges.append(edge)

        return edge

    def generate_patterns(self, minimum_dots: int = 4) -> List[List[int]]:
        result = []

        for i in range(len(self.dots)):
            self.__fulfill_pattern(minimum_dots, i, result)

        return result

    def __fulfill_pattern(self, minimum_dots: int, index: int, patterns: List[List[int]], pattern: List[int] = None):
        dot = self.dots[index]
        if pattern is None:
            pattern = [dot.value]
        else:
            pattern.append(dot.value)

        if len(pattern) >= minimum_dots:
            patterns.append(pattern[:])

        indexes = [i for i in dot.adjacency_dots if self.dots[i].value not in pattern]
        if len(indexes) > 0:
            for i in indexes:
                self.__fulfill_pattern(minimum_dots, i, patterns, pattern[:])


# noinspection PyCompatibility
class Dot:
    def __init__(self, value):
        self.value = value
        self.adjacency_dots: List[int] = []
        self.edges: List[Edge] = []


class Edge:
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right


# noinspection PyCompatibility
class TestDotGrid(unittest.TestCase):
    def setUp(self) -> None:
        self.dot_grid = DotGrid()

        self.dot_grid.connect(1, 2)
        self.dot_grid.connect(1, 4)
        self.dot_grid.connect(1, 5)

        self.dot_grid.connect(2, 1)
        self.dot_grid.connect(2, 3)
        self.dot_grid.connect(2, 4)
        self.dot_grid.connect(2, 5)
        self.dot_grid.connect(2, 6)

        self.dot_grid.connect(3, 2)
        self.dot_grid.connect(3, 5)
        self.dot_grid.connect(3, 6)

        self.dot_grid.connect(4, 1)
        self.dot_grid.connect(4, 2)
        self.dot_grid.connect(4, 5)
        self.dot_grid.connect(4, 7)
        self.dot_grid.connect(4, 8)

        self.dot_grid.connect(5, 1)
        self.dot_grid.connect(5, 2)
        self.dot_grid.connect(5, 3)
        self.dot_grid.connect(5, 4)
        self.dot_grid.connect(5, 6)
        self.dot_grid.connect(5, 7)
        self.dot_grid.connect(5, 8)
        self.dot_grid.connect(5, 9)

        self.dot_grid.connect(6, 2)
        self.dot_grid.connect(6, 3)
        self.dot_grid.connect(6, 5)
        self.dot_grid.connect(6, 8)
        self.dot_grid.connect(6, 9)

        self.dot_grid.connect(7, 4)
        self.dot_grid.connect(7, 5)
        self.dot_grid.connect(7, 8)

        self.dot_grid.connect(8, 4)
        self.dot_grid.connect(8, 5)
        self.dot_grid.connect(8, 6)
        self.dot_grid.connect(8, 7)
        self.dot_grid.connect(8, 9)

        self.dot_grid.connect(9, 5)
        self.dot_grid.connect(9, 6)
        self.dot_grid.connect(9, 8)

    def testBasic(self):
        patterns = self.dot_grid.generate_patterns()
        sum_of_4 = [item for item in patterns if 4 == len(item)]
        sum_of_5 = [item for item in patterns if 5 == len(item)]
        sum_of_6 = [item for item in patterns if 6 == len(item)]
        sum_of_7 = [item for item in patterns if 7 == len(item)]
        sum_of_8 = [item for item in patterns if 8 == len(item)]
        sum_of_9 = [item for item in patterns if 9 == len(item)]

        self.assertEqual(len(patterns),
                         len(sum_of_4) + len(sum_of_5) + len(sum_of_6) + len(sum_of_7) + len(sum_of_8) + len(sum_of_9))

        print("total patterns=", len(patterns), "\n",
              "4 dots patterns=", len(sum_of_4), "\n",
              "5 dots patterns=", len(sum_of_5), "\n",
              "6 dots patterns=", len(sum_of_6), "\n",
              "7 dots patterns=", len(sum_of_7), "\n",
              "8 dots patterns=", len(sum_of_8), "\n",
              "9 dots patterns=", len(sum_of_9), "\n",
              )

        print("top 10", patterns[0:10])
        print("last 10", patterns[:-10:-1])


if __name__ == '__main__':
    unittest.main()
