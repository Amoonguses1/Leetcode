# Time: O(n^3)
# Space: O(n^2)


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[float('inf')] * (n+1) for _ in range(n+1)]
        for i in range(n, 0, -1):
            for j in range(i, n+1):
                if i == j:
                    dp[i][j] = 0
                if j - i == 1:
                    dp[i][j] = i
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], max(dp[i][k-1], dp[k+1][j])+k)
        return dp[1][-1]
