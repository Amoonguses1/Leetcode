# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minNum, lenNums = min(nums), len(nums)
        return sum(nums) - lenNums * minNum
