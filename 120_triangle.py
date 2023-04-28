from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """Function to calculate the minimum path sum from top to bottom.

        Args:
            triangle(List[List[int]]): an array following the rules
            len(triangle[0]) = 1
            len(triangle[i]) = len(triangle[i-1]) + 1

        Returns:
            int: the minimum sum
        """
        # bottom-up approach
        # Time: O(n^2)
        # Space: O(n)
        # n = len(triangle)
        """
        r_size = len(triangle)
        dp = [0] * (r_size+1)
        for i in range(r_size-1, -1, -1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]
        """
        # top-down approach
        # Time: O(n^2)
        # Space: O(n^2)
        # n = len(triangle)
        r_size = len(triangle)
        self.dp = [[""] * i for i in range(1, r_size+1)]
        for i in range(r_size):
            self.dp[r_size-1][i] = triangle[r_size-1][i]
        return self.dfs(triangle, 0, 0, r_size)

    def dfs(self, tri_arr, depth, pos, row):
        if self.dp[depth][pos] == "":
            leaf = self.dfs(tri_arr, depth+1, pos, row)
            leaf = min(leaf, self.dfs(tri_arr, depth+1, pos+1, row))
            self.dp[depth][pos] = tri_arr[depth][pos] + leaf
        return self.dp[depth][pos]
