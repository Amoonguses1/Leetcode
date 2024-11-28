# Time: O(MN)
# Space: O(MN)
# M = len(grid), N = len(grid[0])
from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res_max = [[0] * cols for _ in range(rows)]
        res_min = [[0] * cols for _ in range(rows)]
        res_max[0][0] = grid[0][0]
        res_min[0][0] = grid[0][0]
        for i in range(1, cols):
            res_max[0][i] = res_max[0][i-1] * grid[0][i]
            res_min[0][i] = res_min[0][i-1] * grid[0][i]
        for i in range(1, rows):
            res_max[i][0] = res_max[i-1][0] * grid[i][0]
            res_min[i][0] = res_min[i-1][0] * grid[i][0]

        for i in range(1, rows):
            for j in range(1, cols):
                if grid[i][j] > 0:
                    res_max[i][j] = max(
                        res_max[i-1][j], res_max[i][j-1]) * grid[i][j]
                    res_min[i][j] = min(
                        res_min[i-1][j], res_min[i][j-1]) * grid[i][j]
                else:
                    res_min[i][j] = max(
                        res_max[i-1][j], res_max[i][j-1]) * grid[i][j]
                    res_max[i][j] = min(
                        res_min[i-1][j], res_min[i][j-1]) * grid[i][j]
        return res_max[-1][-1] % int(1e9+7) if res_max[-1][-1] >= 0 else -1
