# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec = True, True
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                dec = False
            elif nums[i+1] < nums[i]:
                inc = False
        return inc or dec
