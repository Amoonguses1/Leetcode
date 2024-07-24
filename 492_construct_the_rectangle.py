# Time: O(sqrt(area))
# Space: O(1)
from typing import List
from math import sqrt


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        pair = []
        for i in range(1, int(sqrt(area))+1):
            if area % i == 0:
                pair = [area//i, i]
        return pair
