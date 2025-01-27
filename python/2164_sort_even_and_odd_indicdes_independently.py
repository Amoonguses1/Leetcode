# Time: O(NlogN)
# Space: O(N)
# N = len(nums)
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odds = sorted([nums[i] for i in range(1, len(nums), 2)], reverse=True)
        evens = sorted([nums[i] for i in range(0, len(nums), 2)])
        ans = []
        for i in range(len(nums)):
            if i % 2:
                ans.append(odds[i//2])
            else:
                ans.append(evens[i//2])
        return ans
