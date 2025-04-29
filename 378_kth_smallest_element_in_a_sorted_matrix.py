# time: O(columns * log(matrix[-1][-1] - matrix[0][0]))
# space: O(1)
from typing import List


class Solution:

    def kthSmallest(self, matrix, k):
        row, columns = len(matrix), len(matrix[0])

        def countLessOrEqual(x):
            count = 0
            comparison = columns - 1
            for i in range(row):
                while comparison >= 0 and matrix[i][comparison] > x:
                    comparison -= 1
                count += (comparison + 1)
            return count

        left, right = matrix[0][0] - 1, matrix[-1][-1] + 1
        ans = -1
        while left < right - 1:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid
            else:
                left = mid

        return ans
