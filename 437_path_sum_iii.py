# Time: O(N)
# Space: O(N)
# N is the number of nodes
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.cnt = 0
        self.targetSum = targetSum
        self.dfs(root, True, targetSum)
        return self.cnt

    def dfs(self, root, start, target):
        if not root:
            return

        target -= root.val
        if target == 0:
            self.cnt += 1
        self.dfs(root.left, False, target)
        self.dfs(root.right, False, target)
        if start:
            self.dfs(root.left, start, self.targetSum)
            self.dfs(root.right, start, self.targetSum)
        return
