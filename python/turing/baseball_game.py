#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


def call_points(ops) -> int:
  """
  :type ops: List[str] - List of operations
  :rtype: int - Sum of scores after performing all operations
  """
  scores = []

  for op in ops:
    match op:
      case "+":
        scores.append(scores[-1] + scores[-2])
      case "D":
        scores.append(scores[-1] * 2)
      case "C":
        scores.pop()
      case _:
        scores.append(int(op))

  return sum(scores)


class TestBaseBallGame(unittest.TestCase):
  def testBasic(self):
    self.assertEqual(30, call_points(["5", "2", "C", "D", "+"]))

  def testBasic1(self):
    self.assertEqual(27, call_points(["5", "-2", "4", "C", "D", "9", "+", "+"]))


if __name__ == '__main__':
  unittest.main()
