# Time: O(N)
# Space: O(1)
# N is the length of s
from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        stringDict = defaultdict(lambda: 0)
        for i in range(len(p)):
            stringDict[s[i]] -= 1
            stringDict[p[i]] += 1
        ans = []
        if self.isAnagram(stringDict):
            ans.append(0)
        for i in range(len(p), len(s)):
            stringDict[s[i-len(p)]] += 1
            stringDict[s[i]] -= 1
            if self.isAnagram(stringDict):
                ans.append(i-len(p)+1)
        return ans

    def isAnagram(self, stringDict):
        for value in stringDict.values():
            if value != 0:
                return False
        return True
