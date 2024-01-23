# Time: O(NW)
# Space: O(W)
# W = sum(nums), N = len(nums)
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False

        dp = [True] + [False] * s
        for num in nums:
            for cur in range(s, num-1, -1):
                dp[cur] = dp[cur] or dp[cur-num]
        return dp[s//2]
