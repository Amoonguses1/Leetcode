# Time: O(row*col)
# Space: O(col)
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """Function to find a path from top left to bottom right,
        which minimizes the sum of all numbers along its path

        Args:
            grid(List[List[int]]): the cost to path through the position.

        Returns:
            int: the minimum cost of the path
            from top-left corner to bottom-right corner
        """
        row, col = len(grid), len(grid[0])
        dp = [0] * col
        dp[0] = grid[0][0]
        for i in range(row):
            if i > 0:
                dp[0] += grid[i][0]
            for j in range(1, col):
                if i == 0:
                    dp[j] = grid[i][j] + dp[j-1]
                else:
                    dp[j] = grid[i][j] + min(dp[j-1], dp[j])
        return dp[-1]
