# Time: O(N)
# Space: O(1)
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """Find thelargest sum without any adjacent elements.

        Given an integer array nums, return the maximum amount of
        the sum without choosing any adjacent elements.

        Args:
            nums(List[int]): an integer array

        Returns:
            int: the largest sum under the condition
        """
        old, tmp = 0, 0
        for num in nums:
            old, tmp = tmp, max(old+num, tmp)
        return tmp
