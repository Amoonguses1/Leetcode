# Time: O(NlogN)
# Space: O(N)
# N = len(points)
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[1])
        cnt, pos = 0, -float("inf")
        for xstart, xend in points:
            if xstart > pos:
                pos = xend
                cnt += 1
        return cnt
