# Time: O(N)
# Space: O(MN)
# M = len(text1), N = len(text2)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2)+1)
        prev = [0] * (len(text2)+1)
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[j+1] = prev[j] + 1
                else:
                    dp[j+1] = max(prev[j+1], dp[j])
            prev = dp[:]
        return dp[-1]
