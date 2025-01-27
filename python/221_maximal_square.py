# Time: O(M*N)
# Space: O(M*N)
# M = len(matrix[0]), N = len(matrix)
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """Find the largest square size

        Given an m x n binary matrix filled with 0's and 1's,
        find the largest square containing only 1's and return its area.

        Args:
            matrix(List[List[int]]): M * N matrix filled with 0's and 1's.

        Returns:
            int: the area of hte largest square
        """
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        size = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                size = max(size, dp[i][j])
        return size ** 2
