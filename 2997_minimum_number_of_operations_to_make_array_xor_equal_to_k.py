# Time: O(NlogM)
# Space: O(1)
# N = len(nums) M is the maximum number of nums
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        ans = 0
        while k or xor:
            if (k % 2) != (xor % 2):
                ans += 1

            k //= 2
            xor //= 2
        return ans
