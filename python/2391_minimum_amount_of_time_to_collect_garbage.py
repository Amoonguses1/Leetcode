# Time: O(N)
# Space: O(1)
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        for items in garbage:
            res += len(items)

        found = {"M": 0, "P": 0, "G": 0}
        for i in range(len(travel), 0, -1):
            for ch in "MPG":
                found[ch] = found[ch] or ch in garbage[i]
            res += travel[i-1] * (sum(found.values()))
        return res
