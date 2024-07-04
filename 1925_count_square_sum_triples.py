# Time: O(n^2)
# Space: O(1)
from math import isqrt


class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1, n):
            for j in range(i+1, n):
                cur = i*i + j*j
                if cur == isqrt(cur)**2 and isqrt(cur) <= n:
                    ans += 2
        return ans
