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
    def leafSimilar(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        root1Leaves = self.getLeaves(root1)
        root2Leaves = self.getLeaves(root2)
        return root1Leaves == root2Leaves

    def getLeaves(self, root):
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [root.val]

        return self.getLeaves(root.left) + self.getLeaves(root.right)
