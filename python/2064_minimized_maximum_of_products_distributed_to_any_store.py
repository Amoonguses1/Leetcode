# Time: O(nlogM)
# Space: O(1)
# M = max(quantities)
from typing import List
from math import ceil


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)

        while left < right:
            mid = (left+right) // 2
            cnt = self.distributeCnt(mid, quantities)
            if cnt <= n:
                right = mid
            else:
                left = mid + 1
        return left

    def distributeCnt(self, num, quantities):
        cnt = 0
        for quantity in quantities:
            cnt += ceil(quantity / num)
        return cnt
