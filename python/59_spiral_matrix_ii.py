# Time: O(pow(n, 2))
# Space: O(pow(n, 2))
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """Function generate an n x n matrix filled with elements
        from 1 to n ** 2 in spiral order.

        Args:
            n(int): a natural number which stands for return matrix size

        Returns:
            List[List[int]]: an n x n matrix filled with elements
            from 1 to n ** 2 in spiral order
        """
        matrix = [[0]*n for _ in range(n)]
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        d = 0
        y, x = 0, 0
        for i in range(1, n*n+1):
            matrix[y][x] = i
            dy, dx = directions[d % 4]
            if -1 < y+dy < n and -1 < x+dx < n and matrix[y+dy][x+dx] == 0:
                y, x = y+dy, x+dx
            else:
                d += 1
                dy, dx = directions[d % 4]
                y, x = y+dy, x+dx
        return matrix
