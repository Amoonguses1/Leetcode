# Time: O(MN)
# Space: O(MN)
# M = len(isWater), N = len(isWater[0])
from collections import deque


class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        rows, cols = len(isWater), len(isWater[0])
        heights = [[-1] * cols for _ in range(rows)]

        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    queue.append((i, j, 0))
                    heights[i][j] = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            x, y, height = queue.popleft()
            for difX, difY in directions:
                nx, ny = x + difX, y + difY

                if 0 <= nx < rows and 0 <= ny < cols and heights[nx][ny] < 0:
                    heights[nx][ny] = height + 1
                    queue.append((nx, ny, height+1))

        return heights
