# Time: O(MN^2)
# Space: O(N)
# M = len(grid), N = len(grid[0])
from typing import List


class Solution:
    def minPathCost(
            self,
            grid: List[List[int]],
            moveCost: List[List[int]]
    ) -> int:
        dp = grid[0].copy()
        for i in range(1, len(grid)):
            cur_dp = grid[i].copy()
            for j in range(len(grid[0])):
                cost = float("inf")
                for k in range(len(grid[0])):
                    cost = min(cost, dp[k]+moveCost[grid[i-1][k]][j])
                cur_dp[j] += cost
            dp = cur_dp
        return min(dp)
