# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Function to remove some duplicates in-place such that
        each unique element appears at most twice
            Args:
                nums(List[int]): non-decreasing order list
            Returns:
                int: the length of the list removed some duplicated element
        """
        if not nums:
            raise ValueError("nums must be a list")

        check = -10**4
        for num in nums:
            if not isinstance(num, int) or num < check:
                raise ValueError("nums must be a non-decreasing order list")

            check = num

        k = 0
        for num in nums:
            if k < 2 or num != nums[k-2]:
                nums[k] = num
                k += 1
        return k
