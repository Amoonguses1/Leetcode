# Time: O(MN)
# Space: 0(N)
# M = len(points), N = len(queries)
from typing import List


class Solution:
    def countPoints(
            self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        res = []
        for x, y, rad in queries:
            cnt = 0
            for pointX, pointY in points:
                if (pointX-x)**2 + (pointY-y)**2 <= rad**2:
                    cnt += 1
            res.append(cnt)
        return res
