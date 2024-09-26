from typing import List
import collections
from bisect import bisect_left, bisect_right


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        # Time: O(logN)
        # Space: O(1)
        # N = len(nums)
        n = len(nums)
        i = nums[n // 2]
        cnt = bisect_right(nums, i) - bisect_left(nums, i)
        return max(n % 2, 2 * cnt - n)

    def minLengthAfterRemovals2(self, nums: List[int]) -> int:
        # Time: O(N+M)
        # Space: O(M)
        # N = len(nums) M is the number of distinct elements
        cnt = collections.Counter(nums)
        maxNum = max(cnt.values())
        n = len(nums)
        if maxNum <= n // 2:
            return n % 2

        return (maxNum-n//2) * 2 - n % 2
