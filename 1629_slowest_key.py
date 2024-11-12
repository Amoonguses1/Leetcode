# Time: O(N)
# Space: O(1)
# N = len(releaseTimes)
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        duration = releaseTimes[0]
        res = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            cur = releaseTimes[i] - releaseTimes[i-1]
            ch = keysPressed[i]
            if cur > duration or (cur == duration and ch > res):
                res = ch
                duration = cur
        return res
