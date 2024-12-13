# Time: O(NlogN)
# Space: O(N)
# N = len(cost)
from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        res = 0
        prices = sorted(cost, reverse=True)
        for i, price in enumerate(prices):
            if (i+1) % 3 != 0:
                res += price
        return res
