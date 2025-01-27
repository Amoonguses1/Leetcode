# Time: O(rows*cols)
# Space: O(rows*cols)
from typing import List


class Solution:
    def spiralMatrixIII(
            self,
            rows: int,
            cols: int,
            rStart: int,
            cStart: int
    ) -> List[List[int]]:
        x, y = rStart, cStart
        dirX, dirY = 0, 1
        twice = 2
        res = []
        moves, next_moves = 1, 2

        while len(res) < rows * cols:
            if self.isInner(x, y, rows, cols):
                res.append([x, y])

            x += dirX
            y += dirY
            moves -= 1

            if moves == 0:
                dirX, dirY = dirY, -1*dirX
                twice -= 1
                if twice == 0:
                    twice = 2
                    moves = next_moves
                    next_moves += 1
                else:
                    moves = next_moves - 1

        return res

    def isInner(self, x, y, rows, cols):
        return -1 < x < rows and -1 < y < cols
