# Time: O(N)
# Space: O(N)
# N = len(nums)
from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        cur, target = 0, pow(2, maximumBit) - 1
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            cur ^= num
            res[len(nums)-1-i] = cur ^ target
        return res
