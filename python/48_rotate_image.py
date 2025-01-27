# Time: O(N**2)
# Space: O(1)
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Function to rotate the image by 90 degrees(clockwise)

        Args:
            matrix(List[List[int]]): an array consist of integer

        Returns:
            None: return nothing, rotate image in-place
        """
        # two step solution
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        """
        # one step solution
        size = len(matrix)
        cntr = size // 2
        for i in range(cntr):
            for j in range(i, size-1-i):
                tmp = matrix[i][j]
                for _ in range(4):
                    if size % 2:
                        i, j = j, 2*cntr-i
                    else:
                        i, j = j, 2*cntr - 1 - i
                    nxt = matrix[i][j]
                    matrix[i][j], tmp = tmp, nxt
