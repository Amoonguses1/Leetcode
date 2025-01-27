# Time: O(MN)
# Space: O(MN)
# M = len(board), N = len(board[0])
from typing import List


class Solution:
    def updateBoard(
            self,
            board: List[List[str]],
            click: List[int]
    ) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        self.recursiveRevealing(board, click)
        return board

    def recursiveRevealing(
            self,
            board: List[List[str]],
            click: List[int]
    ) -> List[List[str]]:
        stack = set()
        stack.add(tuple(click))
        while stack:
            x, y = stack.pop()
            count = self.countBombs(board, x, y)
            if count == 0:
                board[x][y] = "B"
                self.addSearchPoints(board, x, y, stack)
            else:
                board[x][y] = str(count)

    def countBombs(
            self,
            board: List[List[str]],
            x: int,
            y: int
    ) -> int:
        cnt = 0
        diff = [(0, 1), (1, 0), (0, -1), (-1, 0),
                (-1, -1), (-1, 1), (1, 1), (1, -1)]
        for diff_x, diff_y in diff:
            nx, ny = x + diff_x, y + diff_y
            if self.isValidPos(board, nx, ny):
                cnt += board[nx][ny] == "M"

        return cnt

    def addSearchPoints(
            self,
            board: List[List[str]],
            x: int,
            y: int,
            stack: set[tuple]
    ):
        diff = [(0, 1), (1, 0), (0, -1), (-1, 0),
                (-1, -1), (-1, 1), (1, 1), (1, -1)]
        for diff_x, diff_y in diff:
            nx, ny = x + diff_x, y + diff_y
            if self.isValidPos(board, nx, ny) and board[nx][ny] == "E":
                stack.add((nx, ny))

    def isValidPos(
            self,
            board: List[List[str]],
            x: int,
            y: int
    ):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
