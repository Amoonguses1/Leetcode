# n = len(nums)
# time: O(logn)
# space: O(1)
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        """Function to find target from list

        Args:
            nums(List[int]): list of integer
            target(int): integer

        Return:
            int: an index of target
        """
        if not nums:
            raise ValueError("nums should not be empty.")

        if target is None:
            raise ValueError("target should not be empty.")

        left = -1
        right = len(nums)
        while left < right - 1:
            now = (left+right)//2
            if nums[now] == target:
                return now
            elif nums[now] > target:
                right = now
            else:
                left = now
        return -1  # -1 means target doesn't exist in nums.
