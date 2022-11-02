#time: O(logN)
#space O(1)
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        n = len(nums) - 1
        right = n
        while left < right:
            mid = ( left + right ) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        # nums[right] is smallest
        if nums[n] < target:
            right -=1
            left = 0
        else:
            left = right
            right = n
        while left <= right:
            mid = ( left + right ) // 2
            if nums[mid] ==target:
                return mid
                
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
