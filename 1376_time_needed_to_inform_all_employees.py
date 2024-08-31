# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def numOfMinutes(
            self,
            n: int,
            headID: int,
            manager: List[int],
            informTime: List[int]
    ) -> int:
        # recursive top down dfs
        children = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m >= 0:
                children[m].append(i)

        def dfs(i):
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]

        return dfs(headID)

    def numOfMinutes2(
            self,
            n: int,
            headID: int,
            manager: List[int],
            informTime: List[int]
    ) -> int:
        # iterative bottom up dfs
        informDict = {headID: informTime[headID]}
        for i in range(n):
            # check if seen before
            if informDict.get(i, -1) != -1:
                continue
            # bottom up
            stack = [i]
            cur = manager[i]
            while informDict.get(cur, -1) == -1:
                stack.append(cur)
                cur = manager[cur]
            while stack:
                time = informDict.get(cur)
                cur = stack.pop()
                informDict[cur] = time + informTime[cur]
        return max(informDict.values())
