# Time: O(N)
# Space: O(1)
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """Function to change to the 'next permutation'
            Args:
                nums(List[int]):an integer list
            Returns:
                None
        """
        if not nums:
            raise ValueError("nums must be a list")

        for num in nums:
            if not isinstance(num, int) or num < 0:
                raise ValueError("nums is a list consist of natural numbers")

        i, j = len(nums) - 1, len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
        else:
            while nums[i-1] >= nums[j]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
            nums[i:] = nums[len(nums)-1:i-1:-1]
