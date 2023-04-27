# Time: O(mn)
# Space: O(mn)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """Function to check whether string s3 is formed
        by an interleaving of s1 and s2.

        Args:
            s1(str): a string
            s2(str): a string
            s3(str): a string

        Returns:
            bool: if string s3 is formed
            by an interleaving of s1 and s2, return True
        """
        # iterative
        """
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[n][m]
        """
        # recursive
        seen = set()
        return self.recursive(s1, s2, s3, seen)

    def recursive(self, s, t, rem, seen):
        if len(s) == len(t) == len(rem) == 0:
            return True

        ans = False
        st, ts = s[1:] + '.' + t, t[1:] + '.' + s
        if len(s) and len(rem) and s[0] == rem[0] and st not in seen:
            seen.add(st)
            ans = self.recursive(s[1:], t, rem[1:], seen)
        if len(t) and len(rem) and t[0] == rem[0] and ts not in seen:
            seen.add(ts)
            ans = ans or self.recursive(s, t[1:], rem[1:], seen)
        return ans
