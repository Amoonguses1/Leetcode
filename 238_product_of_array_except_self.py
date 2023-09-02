# Time: O(N)
# Space: O(N)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """return the array of product of the given array

        Given an integer array nums, return an array answer such that answer[i]
        is equal to the product of all the elements of nums except nums[i].

        Args:
            nums(List[int]): the integer array

        Returns:
            List[int]: the product of the given array
        """
        cur = 1
        res = []
        for i in range(len(nums)):
            res.append(cur)
            cur *= nums[i]
        cur = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= cur
            cur *= nums[i]
        return res
