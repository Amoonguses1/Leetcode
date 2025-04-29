# Time: O(log(columns_num)+log(rows_num))
# Space: O(1)

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Function to search if target is in matrix.
        Args:
            matrix(List[List[int]]): the matrix that may include target
            target(int): the value to be searched
        Return:
            bool: True if target is in matrix
        """
        if not matrix or target is None:
            return False

        row = len(matrix)
        up, down = -1, row
        while up < down - 1:
            mid = (up + down) // 2
            if matrix[mid][0] == target:
                return True

            elif matrix[mid][0] < target:
                up = mid
            else:
                down = mid
        columns = len(matrix[0])
        left, right = -1, columns
        while left < right - 1:
            mid = (left + right) // 2
            if matrix[up][mid] == target:
                return True

            elif matrix[up][mid] < target:
                left = mid
            else:
                right = mid
        return False
