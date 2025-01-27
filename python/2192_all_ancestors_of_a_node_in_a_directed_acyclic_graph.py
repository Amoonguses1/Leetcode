from typing import List
from collections import deque


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Time: O(n+E)
        # Space: O(n+E)
        # E = len(edges)
        ans = [[] for _ in range(n)]
        directChild = [[] for _ in range(n)]
        for e in edges:
            directChild[e[0]].append(e[1])
        for i in range(n):
            self.dfs(i, i, ans, directChild)
        return ans

    def dfs(
            self,
            x: int,
            cur: int,
            ans: List[List[int]],
            directChild: List[List[int]]
    ) -> None:
        for ch in directChild[cur]:
            if not ans[ch] or ans[ch][-1] != x:
                ans[ch].append(x)
                self.dfs(x, ch, ans, directChild)

    def getAncestors2(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Topological sort
        # Time: O(N*2logN + E)
        # E = len(edges)
        parents = [[] for _ in range(n)]
        children = [[] for _ in range(n)]
        indeg = [0] * n
        for parent, child in edges:
            parents[child].append(parent)
            children[parent].append(child)
            indeg[child] += 1

        que = deque()
        for node, indegCnt in enumerate(indeg):
            if indegCnt == 0:
                que.append(node)

        ans = [[] for _ in range(n)]
        while que:
            node = que.popleft()
            li = set()
            for parent in parents[node]:
                li |= set(ans[parent])
                li.add(parent)
            ans[node] = sorted(list(li))

            for child in children[node]:
                indeg[child] -= 1
                if indeg[child] == 0:
                    que.append(child)
        return ans
