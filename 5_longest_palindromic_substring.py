class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Function to find the longest palindromic substring.

            Args:
                s(str): a string

            Returns:
                str: the longest palindromic substring
        """
        # simple dp
        # Time: O(N**2)
        # Space: O(N**2)
        # N = len(s)
        if not isinstance(s, str):
            raise ValueError("Input must be a string")

        """
        dp = [[False] * len(s) for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(len(s)):
                if i + j >= len(s):
                    break
                if s[i] == s[i+j] and (j < 2 or dp[i+1][i+j-1]):
                    dp[i][i+j] = True
                    res = s[i:i+j+1]
                else:
                    dp[i][i+j] = False
        return res
        """
        # Time: O(N**2)
        # Space: O(1)
        # N = len(s)
        res = ""
        for i in range(len(s)):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
