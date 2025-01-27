# Time: O(Nlogk)
# Space: O(k)
# N = len(queries)
from typing import List
from heapq import heappush, heappop


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        heap = []
        ans = []
        for query in queries:
            dist = -1 * (abs(query[0]) + abs(query[1]))
            heappush(heap, dist)
            if len(heap) > k:
                heappop(heap)
            if len(heap) == k:
                ans.append(-1 * heap[0])
            else:
                ans.append(-1)
        return ans
