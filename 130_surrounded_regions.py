# DFS
# Time: O(rows*columns)
# Space: O(rows*columns)
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Function to replace 'O' which is surrounded by 'X'
            with 'X'
            Args:
                board(List[List[str]]): each element of this array
                    is 'O' or 'X'.
            Returns:
                None
        """
        rows = len(board)
        columns = len(board[0])
        if rows < 3 or columns < 3:
            return

        def dfs(row: int, col: int) -> None:
            board[row][col] = 'R'
            if row > 0 and board[row - 1][col] == 'O':
                dfs(row - 1, col)
            if row < rows - 1 and board[row + 1][col] == 'O':
                dfs(row + 1, col)
            if col > 0 and board[row][col - 1] == 'O':
                dfs(row, col - 1)
            if col < columns - 1 and board[row][col + 1] == 'O':
                dfs(row, col + 1)

        for row in range(rows):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][columns - 1] == 'O':
                dfs(row, columns - 1)
        for col in range(1, columns - 1):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[rows - 1][col] == 'O':
                dfs(rows - 1, col)
        for row in range(rows):
            for col in range(columns):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'R':
                    board[row][col] = 'O'
