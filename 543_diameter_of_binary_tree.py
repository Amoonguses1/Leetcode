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
    def __init__(self):
        self.seen = {}

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left, right = self.getDepth(root.left), self.getDepth(root.right)
        cur = left + right
        child = max(self.diameterOfBinaryTree(root.left),
                    self.diameterOfBinaryTree(root.right))
        return max(cur, child)

    def getDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root not in self.seen:
            maxDepth = max(self.getDepth(root.left), self.getDepth(root.right))
            self.seen[root] = maxDepth + 1
        return self.seen[root]
