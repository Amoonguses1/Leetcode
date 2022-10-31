# Time: O(logN)
# Space: O(1)

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        m = len(matrix)
        down = m
        flag = 0
        n = len(matrix[0])
        while up < down:
            mid = (up + down) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                up = mid+1
            else:
                down = mid
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if matrix[up-1][mid] == target:
                return True
            elif matrix[up-1][mid] < target:
                left = mid+1
            else:
                right = mid
        return False