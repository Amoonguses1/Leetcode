# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        dif = abs(goal - sum(nums))
        ans = (dif+limit-1) // limit
        return ans
