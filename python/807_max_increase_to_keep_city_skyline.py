# Time: O(N^2)
# Space: O(N)
# N = len(grid)
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        size = len(grid)
        rows, cols = [0] * size, [0] * size
        for i in range(size):
            for j in range(size):
                rows[i] = max(rows[i], grid[i][j])
                cols[j] = max(cols[j], grid[i][j])

        ans = 0
        for i in range(size):
            for j in range(size):
                ans += min(rows[i], cols[j]) - grid[i][j]
        return ans
