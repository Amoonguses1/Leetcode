# Time: O(N * 2^^N)
# Space: O(N)
# N = len(nums)
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxNum = 0
        for num in nums:
            maxNum |= num

        return self.dfs(nums, 0, maxNum)

    def dfs(self, nums, cur, maxNum):
        ans = 0
        if cur == maxNum:
            ans += 1

        for i, num in enumerate(nums):
            ans += self.dfs(nums[i+1:], cur | num, maxNum)
        return ans
