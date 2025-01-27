from typing import List
# DFS recursive
# Time: O(rows*columns)
# Space: O(1)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Function to cound the number of islands.
            An island is surrounded by water and is formed by
            connecting adjacent lands horizontally or vertically.
            Args:
                grid(List[List[int]]): every element is '1' (island),
                    or '0' (water).
            Returns:
                int: the number of islands
        """
        if not grid:
            return

        rows = len(grid)
        columns = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j, rows, columns)
                    count += 1
        return count

    def dfs(self, map, i, j, rows, columns):
        if -1 < i < rows and -1 < j < columns and map[i][j] == "1":
            map[i][j] = "2"
            self.dfs(map, i-1, j, rows, columns)
            self.dfs(map, i+1, j, rows, columns)
            self.dfs(map, i, j-1, rows, columns)
            self.dfs(map, i, j+1, rows, columns)
