# Time: O(row*col)
# Space: O(col)
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """Function to count the number of unique paths from top-left corner to
        bottom-right corner.

        Args:
            obstacleGrid(List[List[int]]): an integer array grid that tells
            whether there are obstacles or not

        Returns:
            int: the number of unique paths
        """
        col, row = len(obstacleGrid[0]), len(obstacleGrid)
        cur = [0] * col
        cur[0] = 1-obstacleGrid[0][0]
        for i in range(1, col):
            cur[i] = cur[i-1] * (1-obstacleGrid[0][i])
        for i in range(1, row):
            cur[0] = cur[0] * (1-obstacleGrid[i][0])
            for j in range(1, col):
                cur[j] = (cur[j]+cur[j-1]) * (1-obstacleGrid[i][j])
        return cur[-1]
