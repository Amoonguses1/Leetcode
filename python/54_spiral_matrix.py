from collections import deque
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Function to return all elements of the matrix in spiral order.

        Args:
            matrix(List[List[int]]): an array consist of integer numbers

        Returns:
            List[int]: all elements of the matrix in spiral order
        """
        # mutate input
        # Time: O((m*n)**2)
        # Space: O(m*n)
        # m = len(matrix), n = len(matrix[0])
        """result = []
        while matrix:
            result += matrix.pop(0)
            matrix = (list(zip(*matrix)))[::-1]
        return result
        """
        # simple condition without input mutation
        # Tiem: O(m*n)
        # Space: O(m*n)
        # m = len(matrix), n = len(matrix[0])
        move = deque([[0, 1], [1, 0], [0, -1], [-1, 0]])
        row, col, ans = len(matrix), len(matrix[0]), [matrix[0][0]]
        size, cnt = row * col, 0
        posX, posY = 0, 0
        while len(ans) != size:
            dire = move.popleft()
            if dire == [-1, 0]:
                cnt += 1
            while True:
                posX, posY = posX + dire[0], posY + dire[1]
                if dire == [0, 1] and posY == col - cnt:
                    posY -= 1
                    break
                elif dire == [1, 0] and posX == row - cnt:
                    posX -= 1
                    break
                elif dire == [0, -1] and posY < cnt:
                    posY += 1
                    break
                elif dire == [-1, 0] and posX < cnt:
                    posX += 1
                    break
                ans.append(matrix[posX][posY])
            move.append(dire)
        return ans
