# Time: O(N^2)
# Spacw: O(N)
from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s):
            return 0

        c = Counter(s)
        sub1, sub2 = "", ""
        for i, letter in enumerate(s):
            if c[letter] < k:
                sub1 = self.longestSubstring(s[:i], k)
                sub2 = self.longestSubstring(s[i+1:], k)
                break
        else:
            return len(s)
        return max(sub1, sub2)
