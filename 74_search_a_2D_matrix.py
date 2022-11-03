# N = columns times row
# Time: O(logN)
# Space: O(1)

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = -1
        row = len(matrix)
        down = row
        columns = len(matrix[0])
        while up < down - 1:
            mid = (up + down) // 2
            if matrix[mid][0] == target:
                return True

            elif matrix[mid][0] < target:
                up = mid
            else:
                down = mid
        left = -1
        right = columns
        while left < right - 1:
            mid = (left + right) // 2
            if matrix[up][mid] == target:
                return True

            elif matrix[up][mid] < target:
                left = mid
            else:
                right = mid
        return False
