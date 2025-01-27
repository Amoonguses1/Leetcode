# Time: O(n)
# Space: O(1)
# n = len(moves)


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) % 2 != 0:
            return False

        upDown, leftRight = 0, 0
        for ch in moves:
            if ch == "U":
                upDown += 1
            elif ch == "D":
                upDown -= 1
            elif ch == "L":
                leftRight += 1
            else:
                leftRight -= 1
        return upDown == 0 and leftRight == 0
