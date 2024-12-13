# Time: O(MN)
# Space: O(MN)
# M = len(grid), N = len(grid[0])
from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_size, col_size = len(grid), len(grid[0])
        one_rows, one_cols = [0] * row_size, [0] * col_size
        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == 0:
                    continue
                one_rows[i] += 1
                one_cols[j] += 1

        diff_list = [[-row_size-col_size] * col_size for _ in range(row_size)]
        for i in range(row_size):
            for j in range(col_size):
                diff_list[i][j] += one_rows[i]*2 + one_cols[j]*2
        return diff_list
