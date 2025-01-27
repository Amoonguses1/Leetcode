# Time: O(N)
# Space: O(N)
# N is the number of nodes in the given tree
from typing import Optional
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # BFS
        queue = deque([[root, 0]])
        ans = 0
        while queue:
            node, val = queue.popleft()
            if node is None:
                continue
            if node.left is None and node.right is None:
                ans += val*2 + node.val
            queue.append([node.left, val*2 + node.val])
            queue.append([node.right, val*2 + node.val])
        return ans

    def sumRootToLeaf2(self, root: Optional[TreeNode]) -> int:
        # DFS
        self.ans = 0

        def dfs(node, val):
            if node is None:
                return

            if node.left is None and node.right is None:
                self.ans += val*2 + node.val
                return

            dfs(node.left, val*2 + node.val)
            dfs(node.right, val*2 + node.val)

        dfs(root, 0)
        return self.ans
