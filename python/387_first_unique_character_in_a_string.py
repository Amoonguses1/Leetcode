# Time: O(N)
# Space: O(1)
# N = len(s)
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # hash and set solution
        idxDic = {}
        seen = set()
        for i, ch in enumerate(s):
            if ch not in seen:
                seen.add(ch)
                idxDic[ch] = i
            elif ch in idxDic:
                del idxDic[ch]
        return min(idxDic.values()) if idxDic else -1

    def firstUniqChar2(self, s: str) -> int:
        # counting solution
        count = Counter(s)
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i

        return -1
