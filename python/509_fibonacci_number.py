

class Solution:
    def fib(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        if n == 0:
            return 0
        cur, prev = 1, 0
        for _ in range(n-1):
            nxt = cur + prev
            cur, prev = nxt, cur
        return cur

    def fib2(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        dp = [0, 1]
        for i in range(2, n+1):
            dp.append(dp[-1] + dp[-2])
        return dp[n]
