# Time: O(N)
# Space: O(1)
# N = len(s)
from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        numDic = defaultdict(int)
        streak = 0
        for i in range(len(s)):
            if (ord(s[i-1]) - 96) % 26 == (ord(s[i]) - 97):
                streak += 1
            else:
                streak = 1
            numDic[s[i]] = max(numDic[s[i]], streak)
        return sum(numDic.values())
