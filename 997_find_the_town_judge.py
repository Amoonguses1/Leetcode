# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegs, outdegs = set(), [0] * n
        for indeg, outdeg in trust:
            indegs.add(indeg)
            outdegs[outdeg-1] += 1
        for i in range(n):
            if outdegs[i] == n-1 and i+1 not in indegs:
                return i+1
        return -1
