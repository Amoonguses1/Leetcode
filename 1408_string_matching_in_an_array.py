# Time: O(N*S^2)
# Space: O(N*S^2)
# N = len(words), S is the maximum length of the word in words
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        self.trie = {}
        for word in words:
            for i in range(len(word)):
                self.add(word[i:])
        return [word for word in words if self.get(word)]

    def add(self, word):
        node = self.trie
        for ch in word:
            node = node.setdefault(ch, {})
            node["#"] = node.get("#", 0) + 1

    def get(self, word):
        node = self.trie
        for ch in word:
            if node is None:
                return False

            node = node.get(ch)
        return node["#"] > 1
