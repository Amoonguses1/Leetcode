# time: O(n) n is nums length
# space: O(1)
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)
        while left < right - 1:
            now = (left + right)//2
            if nums[now] == target:
                return now
            elif nums[now] > target:
                right = now
            else:
                left = now
        return -1
