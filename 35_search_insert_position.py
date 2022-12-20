# Time: O(logN)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Function to find index if the target is found. If not,
            the index where it would be if it were inserted in order.
            Args:
                nums(List[int]): the list of integers in ascending order
                target(int): the target integer
            Returns:
                int: if target is in the list, the index of the targete
                    in the list, else the index if it were inserted in order.
        """
        left = -1
        right = len(nums)
        while left < right - 1:
            now = (right+left) // 2
            if nums[now] == target:
                return now
            elif nums[now] < target:
                left = now
            else:
                right = now
        return right
