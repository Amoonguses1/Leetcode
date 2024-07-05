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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # iterative dfs solution
        if root is None:
            return 0

        stack = [(root, False)]
        ans = 0
        while stack:
            node, isLeft = stack.pop()
            if node is None:
                continue

            if node.left is None and node.right is None and isLeft:
                ans += node.val
            else:
                stack.append((node.left, True))
                stack.append((node.right, False))
        return ans

    def sumOfLeftLeaves2(self, root: Optional[TreeNode]) -> int:
        # recursive dfs solution
        if root is None:
            return 0

        ans = 0
        if root.left:
            if root.left.left is None and root.left.right is None:
                ans += root.left.val
            else:
                ans += self.sumOfLeftLeaves(root.left)
        ans += self.sumOfLeftLeaves(root.right)
        return ans
