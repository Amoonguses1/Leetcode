from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """Function to count nagetive numbers
        Args:
            grid(list[list[int]]): list of integer
            sorted in non-increasing order both row-wise and column-wise
        Returns:
            int: the number of negative numbers in list
        """
        """
        # binary search
        # time O(rows*log(columns))
        # space O(1)
        # rows=len(grid)
        # columns = len(grid[0])

        if grid is None:
          return 0

        count = 0
        rows=len(grid)
        columns = len(grid[0])
        right = columns
        for i in range(rows):
            left=-1
            while right - left > 1:
                mid = (left+right) // 2
                if grid[i][mid] < 0:
                    right = mid
                else:
                    left = mid
            count += columns - right
        return count

        """
        # effective solution in terms of time complexity
        # time O(rows+columns)
        # space O(1)
        # rows=len(grid)
        # columns = len(grid[0])
        i = len(grid) - 1
        j = 0
        count = 0
        while i >= 0 and j < len(grid[0]):
            if grid[i][j] < 0:
                count +=len(grid[0]) - j
                i -= 1
            else:
                j += 1
        return count
