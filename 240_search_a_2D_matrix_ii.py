# Time: O(min(row, columns) + max(row, columns)log(min(row, columns)))
# Space: O(1)
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        columns = len(matrix[0])
        shorter_matrix_size: int
        matrix_type = 0
        if row <= columns:
            shorter_matrix_size = row
            if row < columns:
                matrix_type = 1
        else:
            shorter_matrix_size = columns
            matrix_type = 2
        for i in range(shorter_matrix_size):
            if matrix[i][i] == target:
                return True

            if matrix[i][i] > target:
                up, down, left, right = -1, i + 1, -1, i + 1
                while up < down - 1:
                    mid = (up + down) // 2
                    if matrix[mid][i] == target:
                        return True
                    elif matrix[mid][i] < target:
                        up = mid
                    else:
                        down = mid
                while left < right - 1:
                    mid = (left + right) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        left = mid
                    else:
                        right = mid
        if matrix_type == 1:
            for i in range(shorter_matrix_size - 1, columns):
                if matrix[shorter_matrix_size - 1][i] >= target:
                    up, down = -1, shorter_matrix_size
                    while up < down - 1:
                        mid = (up + down) // 2
                        if matrix[mid][i] == target:
                            return True
                        elif matrix[mid][i] < target:
                            up = mid
                        else:
                            down = mid
        if matrix_type == 2:
            for i in range(shorter_matrix_size - 1, row):
                if matrix[i][shorter_matrix_size - 1] >= target:
                    left, right = -1, shorter_matrix_size
                    while left < right - 1:
                        mid = (left + right) // 2
                        if matrix[i][mid] == target:
                            return True
                        elif matrix[i][mid] < target:
                            left = mid
                        else:
                            right = mid
        return False
