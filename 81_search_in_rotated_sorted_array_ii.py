# Time: O(NlogN)
# .sort() method takes O(NlogN)
# Space: O(1)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        left = 0
        right =len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left =mid+1
            else:
                right = mid
        return False