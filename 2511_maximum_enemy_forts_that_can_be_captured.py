# Time: O(N)
# Space: O(1)
# N = len(forts)
from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        capture, slow = 0, 0
        for fast, fort in enumerate(forts):
            if fort:
                if fort == -1*forts[slow]:
                    capture = max(capture, fast-slow-1)
                slow = fast
        return capture
