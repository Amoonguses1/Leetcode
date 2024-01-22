# Time: O(NlogN)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        target = nums[len(nums)//2]
        ans = 0
        for num in nums:
            ans += abs(num-target)
        return ans
