#time: O(n)
#space: O(1)
from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return right
