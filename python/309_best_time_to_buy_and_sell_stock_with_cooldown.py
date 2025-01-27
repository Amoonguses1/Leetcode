# Time: O(N)
# Space: O(1)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cd, sell, hold = 0, 0, -float("inf")
        for price in prices:
            prev_cd, prev_sell, prev_hold = cd, sell, hold
            cd = max(prev_cd, prev_sell)
            sell = prev_hold + price
            hold = max(prev_hold, prev_cd-price)
        return max(sell, cd)
