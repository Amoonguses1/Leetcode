# Time: O(N)
# Space: O(1)
# N = len(arr)
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        index_end = arr[0]
        for i in range(len(arr)):
            index_end = max(index_end, arr[i])
            if i == index_end:
                chunks += 1
        return chunks
