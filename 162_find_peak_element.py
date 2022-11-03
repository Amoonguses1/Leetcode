# time: O(logn) n= len(nums)
# space: O(1)
from typing import List


class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1]:
                if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
                    return mid

                else:
                    left = mid
            else:
                right = mid
        return left
