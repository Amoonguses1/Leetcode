# Time: O(N^2)
# Space: O(N)
# N = len(s)
from typing import List


class Solution:
    def wordBreak(self, s: str, words: List[str]):
        """Function to judge
        whether a string can be segmented by words in dictionary word

        Args:
            s(str): a string
            words(list): a list consist of string

        Returns:
            bool: if a string can be segmented by words in dictionary word,
            return True. Otherwise, return False
        """
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]
