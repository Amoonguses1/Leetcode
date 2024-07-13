# Time: O(N^3)
# Space: O(1)
# N = len(points)
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = 0
        for i in range(len(points)-2):
            base = points[i]
            for j in range(i+1, len(points)-1):
                Ax, Ay = points[j]
                Ax -= base[0]
                Ay -= base[1]
                for k in range(j+1, len(points)):
                    Bx, By = points[k]
                    Bx -= base[0]
                    By -= base[1]
                    cur = Ax*By-Ay*Bx
                    ans = max(ans, abs(cur))
        return ans/2
