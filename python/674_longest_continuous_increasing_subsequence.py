# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans, cnt = 0, 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
        return ans
