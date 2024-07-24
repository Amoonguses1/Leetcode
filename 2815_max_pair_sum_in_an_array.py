# Time: O(NlogM)
# Space: O(1)
# N = len(nums), M is the lergest digit among nums.
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = -1
        maxNum = [-float("inf") for _ in range(9)]
        for num in nums:
            cur = num
            maxDigitNum = 0
            while cur > 0:
                maxDigitNum = max(maxDigitNum, cur % 10)
                cur //= 10
            ans = max(ans, maxNum[maxDigitNum-1] + num)
            maxNum[maxDigitNum-1] = max(maxNum[maxDigitNum-1], num)
        return ans
