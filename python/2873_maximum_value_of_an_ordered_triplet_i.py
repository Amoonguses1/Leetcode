from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # one-pass
        # Time: O(N)
        # Space: O(1)
        # N = len(nums)
        ans = 0
        maxNum, maxDiff = 0, 0
        for num in nums:
            ans = max(ans, maxDiff*num)
            maxDiff = max(maxDiff, maxNum - num)
            maxNum = max(maxNum, num)
        return ans

    def maximumTripletValue2(self, nums: List[int]) -> int:
        # blute force
        # Time: O(N^3)
        # Space: O(1)
        # N = len(nums)
        ans = 0
        maxNum, maxDiff = 0, 0
        for num in nums:
            ans = max(ans, maxDiff*num)
            maxDiff = max(maxDiff, maxNum - num)
            maxNum = max(maxNum, num)
        return ans
