# Time: O(N)
# Space: O(N)
# N = len(arr)
from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countDict = Counter(arr)
        return len(set(countDict.values())) == len(countDict)
