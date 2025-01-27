# time: O(logN) N is the size of nums
# space: O(1)
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = -1
        nums_length = len(nums)
        right = nums_length
        exist_flag = True
        indices_list = [-1, -1]
        # find min
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
                if nums[mid] == target:
                    exist_flag = False
            else:
                left = mid
        if exist_flag:
            return indices_list

        indices_list[0] = right
        left = -1
        right = nums_length
        # find max
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        indices_list[1] = left
        return indices_list
