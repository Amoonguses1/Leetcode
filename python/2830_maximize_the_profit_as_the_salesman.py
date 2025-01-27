# Time: O(n+M)
# Space: O(M)
# M = len(offers)
from typing import List


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dp = [0] * (n+1)
        m = [[] for _ in range(n)]
        for start, end, gold in offers:
            m[end].append([start, gold])
        for end in range(1, n+1):
            dp[end] = dp[end-1]
            for start, gold in m[end-1]:
                dp[end] = max(dp[end], dp[start] + gold)
        return dp[-1]
