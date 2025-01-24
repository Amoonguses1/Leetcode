# Time: O(V)
# Space: O(E)
# V is the number of vertices.
# E is the number of edges.


class Solution:
    def findSmallestSetOfVertices(
            self, n: int, edges: list[list[int]]
    ) -> list[int]:
        indegree = [0] * n
        for _, out in edges:
            indegree[out] += 1
        return [i for i in range(n) if indegree[i] == 0]
