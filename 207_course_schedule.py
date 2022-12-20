# Time: O(numCourses + Edges)
# Space: O(numCourses + Edges)
# Edges = len(prerequisites)
from typing import List


class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        return self.topoBFS(numCourses, prerequisites)

    def topoBFS(self, numNodes, edgesList):
        adjList = self.buildAdjacencyList(numNodes, edgesList)
        inDegrees = [0] * numNodes
        for v1, _ in edgesList:
            inDegrees[v1] += 1
        queue = []
        for v in range(numNodes):
            if inDegrees[v] == 0:
                queue.append(v)
        count = 0
        topoOrder = []
        while queue:
            v = queue.pop(0)
            topoOrder.append(v)
            count += 1
            for des in adjList[v]:
                inDegrees[des] -= 1
                if inDegrees[des] == 0:
                    queue.append(des)

        if count != numNodes:
            return False

        else:
            return True

    def buildAdjacencyList(self, n, edgesList):
        adjList = [[] for _ in range(n)]
        for c1, c2 in edgesList:
            adjList[c2].append(c1)
        return adjList
