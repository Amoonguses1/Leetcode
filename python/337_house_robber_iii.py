# Time: O(N)
# Space: O(N)
# N is the number of nodes in a binary tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.recursive(root))

    def recursive(self, root):
        if root is None:
            return 0, 0

        left = self.recursive(root.left)
        right = self.recursive(root.right)
        return max(left) + max(right), left[0] + right[0] + root.val
