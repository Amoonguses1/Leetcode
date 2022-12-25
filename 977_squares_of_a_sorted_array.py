from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """Function to sort the squares of each number.
            Args:
                nums(List[int]): non-decreasing order list
            Returns:
                List[int]: non-decreasing order list
        """
        # Time: O(NlogN)
        # Space: O(1)
        # N = len(nums)
        """
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums
        """
        # time: O(N)
        # Space: O(N)
        # N = len(nums)
        nums_size = len(nums)
        for i in range(nums_size):
            nums[i] = nums[i] ** 2
        right = nums_size - 1
        left = 0
        nums_sorted = [0] * nums_size
        index = nums_size - 1
        while left <= right:
            if nums[left] > nums[right]:
                nums_sorted[index] = nums[left]
                left += 1
            else:
                nums_sorted[index] = nums[right]
                right -= 1
            index -= 1
        return nums_sorted
