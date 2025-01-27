# Time: O(M+N)
# Space: O(M+N)
# M is the sum of the length of the word in dictionary
# N = len(sentence)
from typing import List


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            nxt = node.children.get(ch, False)
            if not nxt:
                node.children[ch] = TrieNode()
                nxt = node.children[ch]
            node = nxt
        node.isWord = True

    def search(self, word):
        node = self.root
        for i, ch in enumerate(word):
            if ch not in node.children:
                break
            node = node.children[ch]
            if node.isWord:
                return word[:i+1]
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        words = sentence.split(" ")
        for i, word in enumerate(words):
            val = trie.search(word)
            words[i] = val
        return " ".join(words)
