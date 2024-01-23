# Time: O(N^2)
# Space: O(N)
# N = len(words)
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        char_set = [set(words[i]) for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (char_set[i] & char_set[j]):
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans
