# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i % 10 == num:
                return i
        return -1
