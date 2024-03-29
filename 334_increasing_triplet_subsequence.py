# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small, big = float('inf'), float('inf')
        for num in nums:
            if num <= small:
                small = num
            elif num <= big:
                big = num
            else:
                return True
        return False
