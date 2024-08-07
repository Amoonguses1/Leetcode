# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                cnt += 1
                if i > 1 and nums[i-2] >= nums[i]:
                    nums[i] = nums[i-1]
        return cnt < 2
