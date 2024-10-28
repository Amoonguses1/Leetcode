# Time: O(2^^N)
# Space: O(2^^N)
# N = len(graph)
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        self.ans = []
        self.dfs(graph, [0], n)
        return self.ans

    def dfs(self, graph, cur, n):
        if cur[-1] == n - 1:
            self.ans.append(cur)
            return

        for nxt in graph[cur[-1]]:
            self.dfs(graph, cur+[nxt], n)
