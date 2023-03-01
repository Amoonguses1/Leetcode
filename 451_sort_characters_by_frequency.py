# Time: O(nlogn)
# Space: O(n)
# n = len(s)
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        """Function sort the given string in decreasing order
        based on the frequency of the characters.

        Args:
            s(str): a string

        Returns:
            str: the sorted string
        """
        str_dic = Counter(s)
        result = []
        for key, val in sorted(str_dic.items(),
                               key=lambda x: x[1], reverse=True):
            result.append(key*val)
        return ''.join(result)
