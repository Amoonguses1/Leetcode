# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        slow = 0
        cnt = k
        for fast in range(len(nums)):
            cnt -= 1 - nums[fast]
            if cnt < 0:
                cnt += 1 - nums[slow]
                slow += 1
        return fast - slow + 1
