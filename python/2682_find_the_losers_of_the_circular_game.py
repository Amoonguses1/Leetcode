# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        curPos = 0
        seen = set([0])
        for i in range(1, n+1):
            curPos = (curPos+i*k) % n
            if curPos not in seen:
                seen.add(curPos)
            else:
                break
        losers = []
        for i in range(n):
            if i not in seen:
                losers.append(i+1)
        return losers
