# Time: O(N^2)
# Space: O(N)
# N = len(matrix)
from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        valid = set([i+1 for i in range(n)])
        for i in range(n):
            if set(matrix[i]) != valid:
                return False
        for j in range(n):
            check = set()
            for j in range(n):
                check.add(matrix[j][i])
            if check != valid:
                return False
        return True
