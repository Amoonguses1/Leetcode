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
    def findTilt(self, root: Optional[TreeNode]) -> int:
        # DFS
        def helper(node):
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)
            self.ans += abs(left-right)
            return node.val + left + right

        self.ans = 0
        helper(root)
        return self.ans
