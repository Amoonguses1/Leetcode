from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # Time: O(N)
        # Space: O(1)
        # N = len(nums)
        for i in range(len(nums)):
            if nums[i] == nums[i-1] or nums[i] == nums[i-2]:
                return nums[i]

    def repeatedNTimes2(self, nums: List[int]) -> int:
        # hash set
        # Time: O(N)
        # Space: O(N)
        # N = len(nums)
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
