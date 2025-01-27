# Time: O(N)
# Space: O(N)
# N = len(nums)
from typing import List


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n, ans = len(nums), 0
        pref, suf = [0] * (n+1), [0] * (n+1)
        for i in range(1, n):
            pref[i] = pref[i-1] | nums[i-1]
            suf[n-i-1] = suf[n-i] | nums[n-i]
        for i in range(n):
            ans = max(ans, pref[i] | suf[i] | nums[i] << k)
        return ans
