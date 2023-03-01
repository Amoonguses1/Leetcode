# Time: O(nlogn)
# Space: O(n)
# n = len(words)
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """Function to return the k most frequent strings.

        Args:
            words(List[str]): a list consist of various words
            k(int): an integer

        Returns:
            List[str]: a list of the k most frequent strings
            """
        dict_words = Counter(words)
        res = sorted(dict_words, key=lambda x: (-dict_words[x], x))
        return res[:k]
