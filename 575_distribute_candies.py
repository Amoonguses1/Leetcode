# Time: O(N)
# Space: O(N)
# N = len(candyType)
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))
