# Time: O(MN)
# Space: O(MN)
# M = len(mat), N = len(mat[0])
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        depth = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i + j not in depth:
                    depth[i+j] = [mat[i][j]]
                else:
                    depth[i+j].append(mat[i][j])
        ans = []
        for entry in depth.items():
            if entry[0] % 2 == 0:
                ans += entry[1][::-1]
            else:
                ans += entry[1]
        return ans
