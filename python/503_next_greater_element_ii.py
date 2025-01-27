# Time: O(N)
# Space: O(N)
# N = len(nums)
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stack = []
        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                pos, _ = stack.pop()
                ans[pos] = num
            stack.append((i, num))

        for num in nums:
            while stack and stack[-1][1] < num:
                pos, _ = stack.pop()
                ans[pos] = num
        return ans
