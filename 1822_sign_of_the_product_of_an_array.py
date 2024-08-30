# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for num in nums:
            if num == 0:
                return 0

            if num < 0:
                ans *= -1
        return ans
