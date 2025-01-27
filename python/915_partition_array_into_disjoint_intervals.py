# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = right_max = nums[0]
        partition = 0
        for i in range(1, len(nums)):
            right_max = max(right_max, nums[i])
            if nums[i] < left_max:
                left_max = right_max
                partition = i
        return partition + 1
