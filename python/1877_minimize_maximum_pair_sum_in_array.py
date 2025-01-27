from typing import List
from collections import defaultdict


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Time: O(N+M)
        # Space: O(N)
        # N = len(nums)
        # M is the range that the elements of nums can take
        frequency = defaultdict(int)
        low = float("inf")
        high = -float("inf")
        for num in nums:
            frequency[num] += 1
            low = min(low, num)
            high = max(high, num)
        ans = 0
        while low <= high:
            if frequency[high] == 0:
                high -= 1
                continue
            if frequency[low] == 0:
                low += 1
                continue
            cur = low + high
            ans = max(ans, cur)
            frequency[low] -= 1
            frequency[high] -= 1
        return ans

    def minPairSum2(self, nums: List[int]) -> int:
        # Time: O(NlogN)
        # Space: O(N)
        # N = len(nums)
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n//2):
            cur = nums[i] + nums[n-i-1]
            ans = max(ans, cur)
        return ans
