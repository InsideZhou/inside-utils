#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


def is_valid(s: str) -> bool:
  """
  :type s: str - String to be tested for validity
  :rtype: bool - Returns true if the string is valid else false
  """
  validation_stack = []
  for c in s:
    if 0 == len(validation_stack):
      validation_stack.append(c)
      continue

    match c:
      case ")":
        tail = validation_stack.pop()
        if "(" != tail:
          return False
      case "]":
        tail = validation_stack.pop()
        if "[" != tail:
          return False
      case "}":
        tail = validation_stack.pop()
        if "{" != tail:
          return False
      case _:
        validation_stack.append(c)

  return 0 == len(validation_stack)


class TestValidParentheses(unittest.TestCase):
  def testBasic(self):
    self.assertTrue(is_valid("{[()(([{}])[]){}]}"))

  def testBasic1(self):
    self.assertFalse(is_valid("{[()(([{]})[]){}]}"))


if __name__ == '__main__':
  unittest.main()
