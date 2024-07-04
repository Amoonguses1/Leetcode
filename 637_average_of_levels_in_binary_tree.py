# Time: O(N)
# Space: O(N)
# N is the number of nodes
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS solution
        ans = []
        q = deque()
        q.append(root)
        while q:
            level = []
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                ans.append(sum(level)/len(level))
        return ans

    def averageOfLevels2(self, root: Optional[TreeNode]) -> List[float]:
        # DFS solution
        valPerLevel = []
        self.dfs(root, 0, valPerLevel)
        ans = []
        for level in valPerLevel:
            ans.append(sum(level)/len(level))
        return ans

    def dfs(self, node, level, arr):
        if not node:
            return

        if len(arr) == level:
            arr.append([node.val])
        else:
            arr[level].append(node.val)
        self.dfs(node.left, level+1, arr)
        self.dfs(node.right, level+1, arr)
        return
