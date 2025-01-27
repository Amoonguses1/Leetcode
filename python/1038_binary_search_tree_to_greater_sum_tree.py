# Time: O(N)
# Space: O(height)
# N is the number of nodes. height is the height of the tree.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root, val):
            if root.right:
                val = helper(root.right, val)
            root.val += val
            val = root.val
            if root.left:
                val = helper(root.left, root.val)
            return val

        helper(root, 0)
        return root
