# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        ans, inc = 0, 0
        for i in range(len(nums)):
            ans += i * nums[i]
            inc += nums[i]
        cur = ans
        for i in range(len(nums)-1, 0, -1):
            cur += inc - len(nums)*nums[i]
            ans = max(ans, cur)
        return ans
