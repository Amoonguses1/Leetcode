# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curSum = res = 0
        for i, num in enumerate(nums):
            if i == 0 or num > nums[i-1]:
                curSum += num
            else:
                curSum = num
            res = max(res, curSum)
        return res
