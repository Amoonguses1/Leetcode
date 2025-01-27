# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums) - 1):
            if (i + cnt) % 2 != 0:
                continue
            if nums[i] == nums[i+1]:
                cnt += 1
        if (len(nums) - cnt) % 2:
            cnt += 1
        return cnt
