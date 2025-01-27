# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = ans = sum(nums[:k])
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i-k]
            ans = max(ans, cur)
        return ans / k
