# Time: O(MN)
# Space: O(MN)
# M = len(mat), N = len(mat[0])
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat) * len(mat[0]):
            return mat

        newMat = [[0] * c for _ in range(r)]
        for i in range(r*c):
            newMat[i//c][i % c] = mat[i//len(mat[0])][i % len(mat[0])]
        return newMat
