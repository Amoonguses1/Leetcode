# Time: O(1)
# Space: O(1)
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] >= rec2[2] or rec1[1] >= rec2[3]:
            return False

        if rec2[0] >= rec1[2] or rec2[1] >= rec1[3]:
            return False

        return True
