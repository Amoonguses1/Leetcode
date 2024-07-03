# Time: O(N^2)
# Space: O(1)
# N = len(nums)
from typing import List
from math import gcd


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            num1 = nums[i] % 10
            for j in range(i):
                num2 = int(str(nums[j])[0])
                if gcd(num1, num2) == 1:
                    ans += 1
        return ans
