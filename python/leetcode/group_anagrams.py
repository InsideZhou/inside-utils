#!/usr/bin/env python
# https://leetcode.cn/problems/group-anagrams/
import unittest
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = {}

    for word in strs:
        key = ''.join(sorted(word))
        words = groups.get(key, [])
        words.append(word)
        words.sort()

        groups[key] = words

    result = [item for item in groups.values()]
    result.sort()
    return  result


class TestGroupAnagrams(unittest.TestCase):
    def test_basic(self):
        self.assertEqual([['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']],
                         group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

        self.assertEqual([[""]], group_anagrams([""]))
        self.assertEqual([["a"]], group_anagrams(["a"]))


if __name__ == '__main__':
    unittest.main()
