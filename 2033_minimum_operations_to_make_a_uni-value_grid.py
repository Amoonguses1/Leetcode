# Time: O(NlogN)
# Space: O(N)
# N = m*n, M = len(grid), n = len(grid[0])
from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flatten = []
        for arr in grid:
            flatten += arr
        flatten.sort()
        n = len(flatten)
        target = flatten[n // 2]
        ans = 0
        for val in flatten:
            cur = abs(val - target)
            if cur % x:
                return -1
            ans += cur // x
        return ans
