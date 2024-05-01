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
from typing import List, Optional, Set


# 关键点为两个：
# 1、图数据结构的建立，顶点、边。
# 2、图顶点的遍历。
# noinspection PyCompatibility
class DotGrid:
    def __init__(self, dots_count: int = 9):
        self.dots: List[Optional[Dot]] = [None] * dots_count

        for i in range(dots_count):
            self.dots[i] = Dot(i + 1)

        self.edges = []

    # 图的建立
    def connect(self, entry_value: int, exit_value: int) -> Edge:
        entry_dot = self.dots[entry_value - 1]
        exit_dot = self.dots[exit_value - 1]

        edge = next((e for e in self.edges if e.entry == entry_value and e.exit == exit_value), None)
        if edge is not None:
            return edge

        edge = Edge(entry_value, exit_value)
        self.edges.append(edge)

        entry_dot.exit_dots.add(exit_value)
        exit_dot.entry_dots.add(entry_value)

        return edge

    def generate_patterns(self, minimum_dots: int = 4) -> List[List[int]]:
        result = []

        def trace_dots(dot: Dot, path: List[int] = None):
            if path is None:
                path = [dot.value]
            else:
                path.append(dot.value)

            if len(path) >= minimum_dots:
                result.append(path)

            for val in [val for val in dot.exit_dots if val not in path]:
                trace_dots(self.dots[val - 1], path[:])

        for d in self.dots:
            trace_dots(d)

        return result


# noinspection PyCompatibility
class Dot:
    def __init__(self, value):
        self.value = value
        self.entry_dots: Set[int] = set()
        self.exit_dots: Set[int] = set()

    def adjacent_dots(self) -> Set[int]:
        return self.entry_dots.union(self.exit_dots)


class Edge:
    def __init__(self, entry: int, exit_dot: int):
        self.entry = entry
        self.exit = exit_dot


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

    def testDotGrid(self):
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

        print(f"adjacent dots of 1: {self.dot_grid.dots[0].adjacent_dots()}")
        print(f"adjacent dots of 2: {self.dot_grid.dots[1].adjacent_dots()}")
        print(f"adjacent dots of 5: {self.dot_grid.dots[4].adjacent_dots()}")


if __name__ == '__main__':
    unittest.main()
