# Time: O(N^2)
# Spaca: O(N^3)
# N = len(s)
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """Function to return all possible palindrome partitioning of s

        Args:
            s(str): a string

        Returns:
            List[List[int]]: all possible palindrome partitioning of s
        """
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[0] = [[]]
        for begin in range(n):
            for end in range(begin+1, n+1):
                candi = s[begin:end]
                if candi == candi[::-1]:
                    for each in dp[begin]:
                        dp[end].append(each+[candi])
        return dp[n]
