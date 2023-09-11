# Time: O(N)
# Space: O(1)
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        for i in range(length):
            if citations[length-i-1] < i+1:
                return i
        return length
