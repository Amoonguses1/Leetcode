# Time: O(N)
# Space: O(N)
# N = len(nums)
from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        ans, stack = 0, []
        for i in range(len(nums)-1, -1, -1):
            cur = 0
            while stack and nums[stack[-1][0]] < nums[i]:
                _, v = stack.pop()
                cur = max(cur+1, v)
            ans = max(ans, cur)
            stack.append([i, cur])
        return ans
