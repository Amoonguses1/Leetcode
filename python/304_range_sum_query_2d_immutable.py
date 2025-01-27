# __init__
# Time: O(row*col)
# Space: O(row*col)
# sumRegion
# Time: O(1)
# Space: O(1)
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.sum = [[0] * (col+1) for _ in range(row+1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                self.sum[i][j] = (
                    matrix[i-1][j-1]
                    + self.sum[i-1][j]
                    + self.sum[i][j-1]
                    - self.sum[i-1][j-1]
                    )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.sum[row2+1][col2+1]
                - self.sum[row2+1][col1]
                - self.sum[row1][col2+1]
                + self.sum[row1][col1])
