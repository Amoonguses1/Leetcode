# n= len(nums)
# time: O(logn)
# space: O(1)
from typing import List


class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        """Function to find the index of the element
        which is greater than its both neighbors.
        In this function, both nums[-1] and nums[len(nums)],
        , both ends of lists, are minus infinity.
        
        Args:
            nums(list[int]): list of integer

        Return:
            int: the index of the element
            which is greater than its both neighbors.
        """
        left = -1
        right = len(nums)
        while right - left < 1:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid
        return right
