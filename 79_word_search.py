# Time: O(m*n*k)
# Space: O(1)
# m len(board), n = len(board[0]), k = len(word)
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """Function to return if the given word exists in the grid

        Args:
            board(List[List[int]]): an array whose elements are a character
            word: a string

        Returns:
            bool: if the given word exists in the grid or not
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) \
           or word[0] != board[i][j]:
            return False

        tmp = board[i][j]
        board[i][j] = "#"
        res = self.dfs(board, i+1, j, word[1:]) \
            or self.dfs(board, i-1, j, word[1:]) \
            or self.dfs(board, i, j+1, word[1:]) \
            or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
