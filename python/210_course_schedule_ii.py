from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        """Function to decide the ordering of courses you should
            take to finish all courses
            Args:
                numCourses(int): the number of courses you should take
                prerequisites(List[List[int]]):
                    prerequisites[i] = [a, b] indicates you must take b
                    before you take a.
            Returns:
            List[int]: the ordering of courses
        """
        # DFS iterative
        # Time: O(numCourses + prerequisites)
        # Space: O(numCourses + prerequisites)
        """
        adj_dic = self.buildAdjList(prerequisites)
        Indegree = defaultdict(int)
        for val_li in adj_dic.values():
            for val in val_li:
                Indegree[val] += 1
        stack = []
        for i in range(numCourses):
            if Indegree[i] == 0:
                stack.append(i)
        ans = []
        while stack:
            cur = stack.pop()
            ans.append(cur)
            for val in adj_dic[cur]:
                Indegree[val] -= 1
                if Indegree[val] == 0:
                    stack.append(val)
        if len(ans) == numCourses:
            return ans
        else:
            return []

    def buildAdjList(self, prerequisities):
        adj_dic = defaultdict(list)
        for after, before in prerequisities:
            adj_dic[before].append(after)
        return adj_dic
        """
        # DFS recursive
        # Time: O(numCourses + prerequisites)
        # Space: O(numCourses + prerequisites)
        self.graph = defaultdict(list)
        self.res = []
        for after, before in prerequisites:
            self.graph[after].append(before)
        self.visited = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if not self.dfs(i):
                return []
        return self.res

    def dfs(self, node):
        if self.visited[node] == -1:
            return False

        if self.visited[node] == 1:
            return True

        self.visited[node] = -1
        for i in self.graph[node]:
            if not self.dfs(i):
                return False
        self.visited[node] = 1
        self.res.append(node)
        return True
