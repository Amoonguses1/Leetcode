

class Solution:
    def canWinNim(self, n: int) -> bool:
        # Time: O(n)
        # Space: O(1)
        # dp solution
        # this solution is not acceptable
        # bacause this solution causes Time Limit Exceeded
        if n < 4:
            return True

        dp = [True] * 3
        for i in range(n-3):
            if dp[0] and dp[1] and dp[2]:
                dp = dp[1:3] + [False]
            else:
                dp = dp[1:3] + [True]
        return dp[-1]

    def canWinNim2(self, n: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        return n % 4 != 0
