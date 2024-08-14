# Time: O(N)
# Space: O(N)
# N = len(nums)
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = []
        for i in range(0, len(nums), 2):
            cur = [nums[i+1]] * nums[i]
            decompressed += cur
        return
