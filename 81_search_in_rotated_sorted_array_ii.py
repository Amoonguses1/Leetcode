# Time: O(NlogN) N is the number of nums component
# .sort() method takes O(NlogN)
# Space: O(1)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        left = -1
        right = len(nums)
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        return False
