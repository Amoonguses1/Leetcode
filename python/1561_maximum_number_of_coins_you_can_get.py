# Time: O(NlogN)
# Space: O(N)
# N = len(piles)
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        for i in range(len(piles)//3, len(piles), 2):
            res += piles[i]
        return res
