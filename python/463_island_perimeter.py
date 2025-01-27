# Time: O(MN)
# Space: O(MN)
# M = len(grid), N = len(grid[0])


class Solution:
    def islandPerimeter(
            self, grid: list[list[int]]
    ) -> int:
        x, y = self.findFirstIsland(grid)
        stack = [(x, y)]
        seen = set((x, y))

        perimeter = 0
        while stack:
            x, y = stack.pop()
            if (x, y) in seen:
                continue

            seen.add((x, y))
            nextIsland = self.findNeighborIsland(x, y, grid)
            perimeter += 4 - len(nextIsland)
            stack += nextIsland

        return perimeter

    def findFirstIsland(
            self, grid: list[list[int]]
    ) -> tuple[int]:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return (i, j)

    def findNeighborIsland(
            self, x: int, y: int, grid: list[list[int]]
    ) -> list[tuple[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = []
        for direction in directions:
            nx, ny = x + direction[0], y + direction[1]
            if self.isValidPos(nx, ny, grid) and grid[nx][ny] == 1:
                res.append((nx, ny))
        return res

    def isValidPos(
            self, x: int, y: int, grid: list[list[int]]
    ) -> bool:
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
