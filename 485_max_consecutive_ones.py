# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # sliding window solution
        left, zeros = 0, 0
        for i, num in enumerate(nums):
            zeros += num == 0
            if zeros > 0:
                zeros -= nums[left] == 0
                left += 1
        return len(nums) - left

    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:
        # greedy solution
        ans, cnt = 0, 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
        return max(ans, cnt)
