# Time: O(V+E)
# Space: O(V+E)
# V is the number of edges in the given graph.
# E is the number of nodes in the given graph.
from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        vectorSize = len(graph)
        parents, indegree = self.constructParentsAndIndegree(vectorSize, graph)

        queue = deque()
        for i in range(vectorSize):
            if indegree[i] == 0:
                queue.append(i)

        safe = [False] * vectorSize
        while queue:
            node = queue.popleft()
            safe[node] = True
            for nextNode in parents[node]:
                indegree[nextNode] -= 1
                if indegree[nextNode] == 0:
                    queue.append(nextNode)

        return [i for i in range(vectorSize) if safe[i]]

    def constructParentsAndIndegree(self, size: int, graph: list[list[int]]):
        indegree = [0] * size
        parents = [[] for _ in range(size)]
        for i in range(size):
            for node in graph[i]:
                parents[node].append(i)
                indegree[i] += 1
        return parents, indegree
