# Time: O(N+k)
# Space: O(k)
# N = len(commands), k = len(obstacles)
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx, dy = 0, 1
        x, y = 0, 0
        ans = 0
        obstacles = set(map(tuple, obstacles))
        for command in commands:
            if command == -2:
                dx, dy = -dy, dx
            elif command == -1:
                dx, dy = dy, -dx
            else:
                for _ in range(command):
                    x += dx
                    y += dy
                    if (x, y) in obstacles:
                        x -= dx
                        y -= dy
                        break
                ans = max(ans, x**2 + y**2)
        return ans
