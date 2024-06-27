# Time: O(N)
# Space: O(1)
# N is the number of nodes
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return -1

        return self.dfs(root, root.val)

    def dfs(self, root, minVal):
        if root is None:
            return -1

        if root.val > minVal:
            return root.val

        left = self.dfs(root.left, minVal)
        right = self.dfs(root.right, minVal)
        if max(left, right) == -1:
            return -1

        if min(left, right) == -1:
            return max(left, right)

        return min(left, right)
