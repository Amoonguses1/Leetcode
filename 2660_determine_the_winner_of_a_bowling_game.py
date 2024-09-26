# Time: O(N)
# Space: O(1)
# N = len(player1) = len(playe2)
from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score1, score2 = 0, 0
        for i, score in enumerate(player1):
            mul = 1
            if i > 0 and player1[i-1] == 10:
                mul = 2
            elif i > 1 and player1[i-2] == 10:
                mul = 2
            score1 += mul*score
        for i, score in enumerate(player2):
            mul = 1
            if i > 0 and player2[i-1] == 10:
                mul = 2
            elif i > 1 and player2[i-2] == 10:
                mul = 2
            score2 += mul*score
        if score1 == score2:
            return 0

        return 1 if score1 > score2 else 2
