#!/usr/bin/env python
# https://leetcode.cn/problems/implement-trie-prefix-tree/
from __future__ import annotations

import string
import unittest
from typing import Optional, List


# 节点的设计需要能识别出到当前节点为止，是否已构成一个词。
class TrieNode:
    base_chars = string.ascii_lowercase
    base_ord = ord(base_chars[0])

    def __init__(self, value: Optional[str], word_stop: bool = False):
        self.value = value
        self.word_stop = word_stop
        self.children: List[Optional[TrieNode]] = [None] * len(TrieNode.base_chars)

    def add_child(self, value: str) -> TrieNode:
        child = TrieNode(value)
        self.children[ord(value) - TrieNode.base_ord] = child
        return child

    def get_child(self, value: str) -> Optional[TrieNode]:
        return self.children[ord(value) - TrieNode.base_ord]


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
        for c in word:
            node = node.get_child(c)
            if node is not None:
                s += node.value
            else:
                break

        return s == word and node.word_stop

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            node = node.get_child(c)
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
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("application"))
        self.assertTrue(trie.search("app"))

    def testStartsWith(self):
        trie = Trie()

        trie.insert("apple")
        self.assertTrue(trie.startsWith("app"))
        self.assertTrue(trie.startsWith("apple"))


if __name__ == '__main__':
    unittest.main()
