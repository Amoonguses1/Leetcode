# Time: O(MN)
# Space: O(MN)
# M = len(grid), N = len(grid[0])
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottenDays = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    self.dfs(grid, rottenDays, [i, j])
        maxDay = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                maxDay = max(maxDay, rottenDays[i][j])
        return -1 if maxDay == float("inf") else maxDay

    def dfs(self, grid, days, pos):
        stack = [[pos[0], pos[1], 0]]
        dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while stack:
            x, y, day = stack.pop()
            days[x][y] = day
            for nxtX, nxtY in dire:
                if (0 > x + nxtX or
                    x + nxtX >= len(grid) or
                    0 > y + nxtY or
                        y + nxtY >= len(grid[0])):
                    continue
                if grid[x+nxtX][y+nxtY] != 1:
                    continue
                if days[x+nxtX][y+nxtY] > day + 1:
                    stack.append([x+nxtX, y+nxtY, day+1])
                    days[x+nxtX][y+nxtY] = day+1
