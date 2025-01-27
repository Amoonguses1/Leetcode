

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """Function to calculate the number of unique paths from the top-left
        corner to the bottom-right corner in the m * n grid.
        restriction
        only move either down or right at any point in time

        Args:
            m(int): the height of the grid
            n(int): the width of the grid

        Returns:
            int: the number of unique paths
        """
        # dp solution
        # Time: O(m*n)
        # Space: O(n)
        """
        cur = [1] * n
        for _ in range(1,m):
            for j in range(1,n):
                cur[j] += cur[j-1]
        return cur[-1]
        """
        # C(m+n-2,n-1)
        # Time: O(min(m,n))
        # Space: O(1)
        smaller = min(m, n)
        ans = 1
        for i in range(smaller-1):
            ans *= m + n - 2 - i
        for i in range(2, smaller):
            ans //= i
        return ans
