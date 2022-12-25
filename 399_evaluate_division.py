# Time: O(N*M)
# Space: O(N)
# N = len(values)
# M = len(queries)

from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        """Function to answer all queries
            Args:
                equations(List[List[str]): equations[i] = [A_i, B_i], A_i and
                    B_i are string.
                values(List[float]): values[i] = A_i / B_i
                queries(List[List[str]]): queries[i] = [C_i, D_i], C_i and
                    D_i are string.
            Returns:
                List[float]: List[i] = C_i / D_i
        """
        # Check input error
        if len(equations) != len(values):
            return

        for li in equations:
            if len(li) != 2:
                return

        for li in queries:
            if len(li) != 2:
                return

        self.G = defaultdict(dict)
        for (x, y), v in zip(equations, values):
            self.G[x][y] = v
            self.G[y][x] = 1/v
        return [self.dfs(s, g, 1, []) for s, g in queries]

    def dfs(self, start: str, goal: str, weight: float, seen: List[str]):
        if goal in self.G[start]:
            return weight * self.G[start][goal]

        seen.append(start)
        for v in self.G[start]:
            if v not in seen:
                cur_weight = self.dfs(v, goal, weight, seen)
                if cur_weight != -1:
                    return cur_weight * self.G[start][v]

        return -1
