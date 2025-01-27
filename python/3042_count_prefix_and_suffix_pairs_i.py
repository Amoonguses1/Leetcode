# Time: O(k*N^2)
# Time: O(1)
# k = max(len(word) for word in words), N = len(words)
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i, word in enumerate(words):
            for j in range(i+1, len(words)):
                if self.isPrefixAndSuffix(word, words[j]):
                    ans += 1
        return ans

    def isPrefixAndSuffix(self, str1, str2):
        if len(str1) > len(str2):
            return False

        return str1 == str2[:len(str1)] and str1 == str2[-len(str1):]
