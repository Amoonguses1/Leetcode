# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow
