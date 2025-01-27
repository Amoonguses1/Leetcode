# Time: O(N)
# Space: O(N)
# N = len(nums)
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        for num in nums:
            seen.add(num)
        ans = []
        for i in range(1, len(nums)+1):
            if i not in seen:
                ans.append(i)
        return ans
