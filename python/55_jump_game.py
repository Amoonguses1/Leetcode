# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Function to check whether you reach the last index

        Args:
            nums(List[int]): maximum jump length at that position

        Returns:
            bool: Return true if you can reach the last index,
            or false otherwise.
        """
        max_index = 0
        for i, num in enumerate(nums):
            if i > max_index:
                return False
            max_index = max(max_index, i+num)
        return True
