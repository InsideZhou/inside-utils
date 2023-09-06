#!/usr/bin/env python
# https://leetcode.cn/problems/implement-trie-prefix-tree/
from __future__ import annotations

import string
import unittest
from typing import Optional, List


class TrieNode:
    def __init__(self, value: Optional[str], chars: str = string.ascii_lowercase):
        self.base_chars = chars
        self.base_ord = ord(chars[0])
        self.word_stop = False
        self.value = value
        self.children: List[Optional[TrieNode]] = [None] * len(chars)

    def add_child(self, value: str) -> TrieNode:
        child = TrieNode(value, self.base_chars)
        self.children[ord(value) - self.base_ord] = child
        return child

    def get_child(self, value: str) -> Optional[TrieNode]:
        return self.children[ord(value) - self.base_ord]


# noinspection PyPep8Naming
class Trie:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            child = node.get_child(c)
            node = child if child is not None else node.add_child(c)

        node.word_stop = True

    def search(self, word: str) -> bool:
        node = self.root
        s = ""
        for index in range(len(word)):
            node = node.get_child(word[index])
            if node is not None:
                s += node.value
            else:
                break

        return s == word and node.word_stop

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for index in range(len(prefix)):
            node = node.get_child(prefix[index])
            if node is None:
                return False

        return True


class TestImplementTriePrefixTree(unittest.TestCase):
    def testInsert(self):
        trie = Trie()

        trie.insert("car")

        self.assertFalse(trie.root.children[2].word_stop)
        self.assertFalse(trie.root.children[2].children[0].word_stop)
        self.assertTrue(trie.root.children[2].children[0].children[17].word_stop)

        self.assertEqual("car", ''.join([
            trie.root.children[2].value,
            trie.root.children[2].children[0].value,
            trie.root.children[2].children[0].children[17].value,
        ]))

        trie.insert("cat")
        self.assertEqual("cat", ''.join([
            trie.root.children[2].value,
            trie.root.children[2].children[0].value,
            trie.root.children[2].children[0].children[19].value,
        ]))

    def testSearch(self):
        trie = Trie()

        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("application"))
        self.assertFalse(trie.search("app"))

        trie.insert("app")
        self.assertTrue(trie.search("app"))

    def testStartsWith(self):
        trie = Trie()

        trie.insert("apple")
        self.assertTrue(trie.startsWith("app"))
        self.assertTrue(trie.startsWith("apple"))


if __name__ == '__main__':
    unittest.main()
