# time: O(logN) N is size of nums
# space O(1)
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left = -1
        nums_length = len(nums) - 1
        right = nums_length
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
        # nums[right] is smallest
        if nums[nums_length] < target:
            left = -1
        else:
            left = right - 1
            right = nums_length + 1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        return -1
