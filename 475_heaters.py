# Time: O(nlogn+ mlogm)
# Space: O(1)
# n = len(houses), m = len(heaters)
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0
        heaterPos, heaterLen = 0, len(heaters)
        for house in houses:
            while heaterPos < heaterLen and house > heaters[heaterPos]:
                heaterPos += 1
            if heaterPos == 0:
                curDist = heaters[0] - house
            else:
                curDist = house - heaters[heaterPos-1]
                if heaterPos != heaterLen:
                    curDist = min(curDist, heaters[heaterPos] - house)
            radius = max(radius, curDist)
        return radius
