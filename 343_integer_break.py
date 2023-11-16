

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # DP
        # Time: O(n^2)
        # Space: O(n)
        """
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[-1]
        """
        # mathmatical approach
        # Time: O(1)
        # Space: O(1)
        if n < 4:
            return n-1

        q, r = n // 3, n % 3
        if r == 0:
            return 3 ** q

        elif r == 1:
            return (3 ** (q-1)) * 4

        else:
            return (3 ** q) * 2
