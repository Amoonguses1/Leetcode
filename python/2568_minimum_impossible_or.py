# Time: O(N)
# Space: O(logN)
# N = len(nums)
from typing import List


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        cur = 1
        numsSet = set()
        for num in nums:
            if num & (num-1) == 0:
                numsSet.add(num)
        while cur in numsSet:
            cur <<= 1
        return cur
