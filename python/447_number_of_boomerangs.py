# Time: O(N^2)
# Space: O(N)
# N = len(points)
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boomerangs = 0
        for posX, posY in points:
            iDist = {}
            for x, y in points:
                dist = (x-posX)**2 + (y-posY)**2
                if dist not in iDist:
                    iDist[dist] = 1
                else:
                    boomerangs += 2*iDist[dist]
                    iDist[dist] += 1
        return boomerangs
