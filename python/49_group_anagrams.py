# Time: O(N)
# Space: O(N)
# N = len(strs)
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Function to find group the anagrams together.
            Args:
                strs(List[str]): a string list
            Returns:
                List[List[str]]: group of the anagrams
        """
        h = defaultdict(list)
        for word in strs:
            h["".join(sorted(word))].append(word)
        return [value for value in h.values()]
