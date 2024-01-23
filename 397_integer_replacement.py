

class Solution:
    def integerReplacement(self, n: int) -> int:
        # Time: O(logn)
        # Space: O(1)
        # mathematical approach
        """
        cnt = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
            cnt += 1
        return cnt
        """
        # recursive approach
        # Time: O(logn)
        # Space: O(logn)
        memo = {}
        return self.helper(n, memo)

    def helper(self, n, memo):
        if n == 1:
            return 0

        if n in memo:
            return memo[n]

        if n % 2 == 0:
            memo[n] = 1 + self.helper(n//2, memo)
        else:
            memo[n] = 1 + min(self.helper(n+1, memo), self.helper(n-1, memo))
        return memo[n]
