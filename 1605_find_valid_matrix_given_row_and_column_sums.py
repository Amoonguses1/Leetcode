# Time: O(MN)
# Space: O(MN)
# M = len(rowSum), N = len(colSum)
from typing import List


class Solution:
    def restoreMatrix(
            self,
            rowSum: List[int],
            colSum: List[int]
    ) -> List[List[int]]:
        res = [[0] * len(colSum) for _ in range(len(rowSum))]
        rPos = cPos = 0
        while rPos < len(rowSum) and cPos < len(colSum):
            res[rPos][cPos] = min(rowSum[rPos], colSum[cPos])
            if rowSum[rPos] < colSum[cPos]:
                colSum[cPos] -= rowSum[rPos]
                rPos += 1
            else:
                rowSum[rPos] -= colSum[cPos]
                cPos += 1
        return res
