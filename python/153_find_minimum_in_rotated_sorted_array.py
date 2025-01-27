# time: O(logn) n is size of nums
# space: O(1)
from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        left = -1
        right = len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
        return nums[right]
