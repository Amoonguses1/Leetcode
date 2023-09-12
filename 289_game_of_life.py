# Time: O(mn)
# Space: O(1)
# m = len(board), n = len(board[0])
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbor = self.search(board, i, j)
                if board[i][j]:
                    if neighbor < 2 or neighbor > 3:
                        board[i][j] = 3
                elif neighbor == 3:
                    board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

    def search(self, arr, x, y):
        row, col = len(arr), len(arr[0])
        res = -1*(1 & arr[x][y])
        for i in range(max(x-1, 0), min(x+2, row)):
            for j in range(max(y-1, 0), min(y+2, col)):
                res += 1 & arr[i][j]
        return res
