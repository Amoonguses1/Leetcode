# Time: O(MN)
# Space: O(MN)
# M = len(heights), N = len(heights[0])
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        p_land = set()
        a_land = set()
        row, col = len(heights), len(heights[0])
        for i in range(row):
            self.spread(i, 0, p_land, row, col, heights)
            self.spread(i, col-1, a_land, row, col, heights)
        for j in range(col):
            self.spread(0, j, p_land, row, col, heights)
            self.spread(row-1, j, a_land, row, col, heights)
        return list(p_land & a_land)

    def spread(self, i, j, land, row, col, matrix):
        land.add((i, j))
        for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
            if (0 <= x < row and 0 <= y < col and
               matrix[x][y] >= matrix[i][j] and (x, y) not in land):
                self.spread(x, y, land, row, col, matrix)
