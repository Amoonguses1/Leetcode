# Time: O(NlogN)
# Space: O(N)
# N = len(nums)
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums)-1) // 2
        lw, hi = nums[:mid+1], nums[mid+1:]
        nums[::2] = lw[::-1]
        nums[1::2] = hi[::-1]
