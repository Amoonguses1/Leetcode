# Time: O(nlogn)
# Space: O(n)
# n = len(nums)
from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = sorted(nums)
        for i in range(len(ans)//2):
            ans[2*i], ans[2*i+1] = ans[2*i+1], ans[2*i]
        return ans
